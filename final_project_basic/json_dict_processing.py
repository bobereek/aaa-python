def extract_nested_value(obj, keys):
    """
    извлекает значение из вложенных структур данных по цепочке ключей
    """
    for key in keys:
        if isinstance(obj, dict) and obj.get(key) is not None:
            obj = obj[key]
        else:
            return None
    return obj


def process_dictionary_with_config(dictionary, config):
    """
    обрабатывает один словарь согласно словару-конфигу
    """

    result = {}
    for new_key, value in config.items():
        if isinstance(value, tuple):
            path, process_func = value
            result[new_key] = process_func(extract_nested_value(dictionary, path))
        else:
            path = value
            result[new_key] = extract_nested_value(dictionary, path)

    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """
    обрабатывает список словарей,
    эта функция нужна чтобы обработать список призов.
    """

    if not list_of_dicts:
        return []
    return [process_dictionary_with_config(d, config) for d in list_of_dicts if d is not None]


def create_processor(config, list_processor=False):
    """
    создает готовый процессор с предзагруженной конфигурацией.
    В случае, если list_processor == True,
    внутрь процессора подается process_list_of_dicts_with_config,
    иначе process_dictionary_with_config.
    """

    if list_processor:

        def processor(data):
            return process_list_of_dicts_with_config(data, config=config)

        return processor

    def processor(data):
        return process_dictionary_with_config(data, config=config)

    return processor
