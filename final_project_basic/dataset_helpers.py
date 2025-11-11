import inspect
from itertools import product


def get_attribute_counts(data):
    """
    Функция для подсчета количества значений в каждом атрибуте
    """
    attribute_counts = {}
    for item in data:
        for key, _ in item.items():
            attribute_counts[key] = attribute_counts.get(key, 0) + 1
    return attribute_counts


def get_none_counts(data, normalized=False):
    """
    Функция для подсчета количества None значений в каждом атрибуте
    """
    none_counts = {}
    for item in data:
        for key, value in item.items():
            if value is None:
                none_counts[key] = none_counts.get(key, 0) + 1

    if normalized:
        attribute_counts = get_attribute_counts(data)

        return {key: round(value / attribute_counts[key], 4) for key, value in none_counts.items()}

    return none_counts


def get_awarded_laureates(data):
    awarded = [laureate for laureate in data if laureate.get("prizes_relevant") is not None]
    return awarded


def get_data_by_id(data, id):
    for item in data:
        if item["id"] == id:
            return item

    return None


def _find_values_recursive(obj, path_parts):
    """
    Функция рекурсивно получает все значения по вложенному пути
    """
    if not path_parts:
        return [obj]

    current_key, rest_of_path = path_parts[0], path_parts[1:]

    if isinstance(obj, dict):
        next_obj = obj.get(current_key)
        if next_obj is not None:
            return _find_values_recursive(next_obj, rest_of_path)
    elif isinstance(obj, list):
        results = []
        for item in obj:
            results.extend(_find_values_recursive(item, path_parts))
        return results

    return []


def filter_by_attribute(data, attribute_path, condition):
    """Фильтрует список словарей по заданному условию для вложенного атрибута.

    Args:
        data: Список словарей для фильтрации.
        path: Путь к атрибуту в виде списка ключей.
        condition: Функция-условие, которая принимает одно значение
        и возвращает True или False.

    Returns:
        list of dict: Отфильтрованный список словарей.

    Примеры использования:
        >>> data = [
        ...     {'name': 'Alice', 'country': 'USA',
        ...      'age': 25, 'prizes': [{'status': 'received'}]},
        ...     {'name': 'Bob', 'country': 'UK',
        ...      'age': 30, 'prizes': [{'status': 'declined'}]}
        ... ]

        # 1. Простой фильтр
        >>> filter_by_attribute(data, ['country'], lambda x: x == 'USA')

        # 2. Сравнение
        >>> filter_by_attribute(data, ['age'], lambda x: x > 28)

        # 3. Вложенный путь
        >>> filter_by_attribute(data, ['prizes', 'status'], lambda x: x == 'declined')
    """
    filtered = []

    for item in data:
        values = _find_values_recursive(item, attribute_path)  # получаем значения аттрибута

        if any(condition(found) for found in values):  # если условие выполняется добавляем
            filtered.append(item)

    return filtered


def group_by(data, attribute_paths, agg=None, agg_attribute=None):
    """Универсально группирует список словарей по одному или нескольким атрибутам.

    Функция может выполнять группировку по одному или нескольким путям.

    Args:
        data: Список словарей для группировки.

        paths: Путь или список путей для группировки.
            - Для одного атрибута: ['path', 'to', 'attribute']
            - Для нескольких атрибутов: [['path1'], ['path2', 'subpath']]

        agg (optional): Агрегирующая функция (например, len или из aggregations.py), которая применяется к каждой группе.
        Если None, возвращаются сами сгруппированные списки.

        agg_attribute (optional): Имя атрибута для агрегации, если функция `agg` принимает два аргумента (как все агрегации из aggregations.py).

    Returns:
        dict: Сгруппированный словарь. Ключами будут значения (для одного атрибута) или кортежи значений (для нескольких атрибутов).

    Примеры использования:
        >>> data = [
        ...     {'country': 'USA', 'type': 'person',
        ...      'prizes': [{'cat': 'Physics'}, {'cat': 'Peace'}]},
        ...     {'country': 'UK', 'type': 'org',
        ...      'prizes': [{'cat': 'Peace'}]}
        ... ]

        # 1. Группировка по одному простому атрибуту ('country')
        >>> group_by(data, ['country'])
        # {'USA': [...], 'UK': [...]}

        # 2. Группировка по одному "сложному" атрибуту ('prizes.cat')
        #    Лауреат из США попадет в обе группы: 'Physics' и 'Peace'.
        >>> group_by(data, ['prizes', 'cat'])
        # {'Physics': [...], 'Peace': [...], ...}

        # 3. Мультигруппировка по нескольким атрибутам ('country' и 'type')
        >>> group_by(data, [['country'], ['type']])
        # {('USA', 'person'): [...], ('UK', 'org'): [...]}

        # 4. Мультигруппировка со "сложным" атрибутом ('country' и 'prizes.cat')
        #    Лауреат из США создаст две группы: ('USA', 'Physics') и ('USA', 'Peace').
        >>> group_by(data, [['country'], ['prizes', 'cat']])
        # {('USA', 'Physics'): [...], ('USA', 'Peace'): [...], ...}
    """
    if not data or not attribute_paths:
        return {}

    grouped = {}

    is_multiple_paths = isinstance(attribute_paths[0], list)
    if not is_multiple_paths:
        # если одиночный путь (['a', 'b']), оборачиваем его в [['a', 'b']]
        attribute_paths = [attribute_paths]

    for item in data:
        values = [_find_values_recursive(item, path) for path in attribute_paths]  # находим все значения аттрибута

        if not all(values):
            continue

        all_keys = product(*values)  # рассматриваем все комбинации для мульти группировки

        for key in all_keys:
            if key not in grouped:
                grouped[key] = []  # создаем отдельную категорию для каждого ключа
            grouped[key].append(item)  # добавляем item этой категории

    if not is_multiple_paths:
        grouped = {key[0]: value for key, value in grouped.items()}

    return __group_by_aggregation(grouped, agg, agg_attribute)  # возвращаем значение функции для агрегации


def __group_by_aggregation(grouped, agg, agg_attribute=None):
    """
    Функция-помощник для агрегации данных после group_by
    """
    if agg is None:
        return grouped

    num_args = len(inspect.signature(agg).parameters)

    if num_args == 1:
        aggregated = {key: agg(group) for key, group in grouped.items()}
        return aggregated

    if num_args == 2:
        assert agg_attribute is not None, f"agg_attribute должен быть задан {agg.__name__}"
        return {key: agg(group, agg_attribute) for key, group in grouped.items()}

    raise ValueError(f"Неподдерживаемая сигнатура агрегации: {agg.__name__} принимает {num_args} аргумента")
