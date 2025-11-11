def add_attribute(laureates_data: list, attribute: str, ids_values: dict):
    """
    Функция добавляет атрибут в список laureates_data
    В словаре ids_values ключ - id, значение - значение атрибута
    attribute - название атрибута
    """
    for laureate in laureates_data:
        if laureate["id"] in ids_values.keys():
            laureate[attribute] = ids_values[laureate["id"]]

    return laureates_data


def remove_attribute(laureates_data, attribute):
    """
    Функция удаляет атрибут из списка laureates_data
    attribute - название атрибута
    """
    for laureate in laureates_data:
        laureate.pop(attribute)
    return laureates_data
