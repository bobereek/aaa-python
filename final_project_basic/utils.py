# я решил вынести обработку года в отдельный файл, так как если оставить ее в laureates_configs.py в соответствии с условием,
# возникнет проблема циклической зависимости, так как в laureates_configs.py импортируется prize_processor из prizes_configs.py
# а в prize_configs.py импортируется process_year из laureates_configs.py
def process_year(year_string):
    """
    извлекает год из строки даты (формат "YYYY-MM-DD")
    """
    if year_string is None:
        return None
    date_string = year_string.split("-")
    return int(date_string[0])
