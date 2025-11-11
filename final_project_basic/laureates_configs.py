from json_dict_processing import create_processor
from prizes_configs import prize_processor
from utils import process_year


CONFIG_PERSON = {
    "id": (["id"], int),
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}

CONFIG_ORG = {
    "id": (["id"], int),
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor()),
}


def person_processor():
    """
    создает процессор для данных о людях-лауреатах
    """
    return create_processor(CONFIG_PERSON, False)


def org_processor():
    """
    создает процессор для данных об организациях-лауреатах
    """
    return create_processor(CONFIG_ORG, False)
