from json_dict_processing import create_processor
from utils import process_year

CONFIG_PRIZE = {
    "prize_amount": ["prizeAmount"],
    "prize_amount_adjusted": ["prizeAmountAdjusted"],
    "award_year": (["awardYear"], process_year),
    "category_en": ["category", "en"],
    "prize_status": ["prizeStatus"],
}


def prize_processor():
    """
    создает процессор для обработки списков призов
    """
    return create_processor(CONFIG_PRIZE, True)
