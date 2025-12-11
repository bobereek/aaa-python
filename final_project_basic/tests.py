# для запуска тестов pytest tests.py

from aggregations import get_mean_by_attribute
from dataset_helpers import filter_by_attribute, group_by
from json_dict_processing import create_processor, extract_nested_value, process_dictionary_with_config

TEST_DICT_PERSON = {
    "id": "123",
    "knownName": {"en": "Test Laureate"},
    "birth": {"date": "1950-01-01", "place": {"country": {"en": "Testland"}}},
    "nobelPrizes": [
        {"awardYear": "2000", "category": {"en": "Physics"}, "prizeAmount": 100},
        {"awardYear": "2010", "category": {"en": "Peace"}, "prizeAmount": 200},
    ],
}

TEST_DATASET = [
    {"id": 1, "country": "USA", "age": 50, "prizes": [{"category": "Physics"}]},
    {"id": 2, "country": "UK", "age": 60, "prizes": [{"category": "Chemistry"}]},
    {"id": 3, "country": "USA", "age": 50, "prizes": [{"category": "Physics"}]},
    {"id": 4, "country": "Germany", "age": 70, "prizes": [{"category": "Peace"}]},
    {
        "id": 5,
        "country": "USA",
        "age": 60,
        "prizes": [{"category": "Peace"}, {"category": "Literature"}],
    },
]


def test_processing_core():
    path = ["birth", "place", "country", "en"]
    expected_country = "Testland"
    assert extract_nested_value(TEST_DICT_PERSON, path) == expected_country

    path_missing = ["birth", "place", "city"]
    assert extract_nested_value(TEST_DICT_PERSON, path_missing) is None

    def process_year_simple(date_str):
        return int(date_str.split("-")[0]) if date_str else None

    test_config = {
        "id_int": (["id"], int),
        "name": ["knownName", "en"],
        "birth_year": (["birth", "date"], process_year_simple),
        "country": ["birth", "place", "country", "en"],
        "non_existent": ["path", "that", "is", "not", "there"],
    }

    processed_dict = process_dictionary_with_config(TEST_DICT_PERSON, test_config)

    assert processed_dict["id_int"] == 123
    assert processed_dict["name"] == "Test Laureate"
    assert processed_dict["birth_year"] == 1950
    assert processed_dict["country"] == "Testland"
    assert processed_dict["non_existent"] is None

    processor = create_processor(test_config)
    processed_via_processor = processor(TEST_DICT_PERSON)
    assert processed_dict == processed_via_processor


def test_helpers_and_aggregations():
    filtered_usa = filter_by_attribute(TEST_DATASET, ["country"], lambda x: x == "USA")
    assert len(filtered_usa) == 3
    assert all(item["country"] == "USA" for item in filtered_usa)

    filtered_age = filter_by_attribute(TEST_DATASET, ["age"], lambda x: x >= 60)
    assert len(filtered_age) == 3

    grouped_by_country = group_by(TEST_DATASET, ["country"])
    assert len(grouped_by_country["USA"]) == 3
    assert len(grouped_by_country["UK"]) == 1
    assert len(grouped_by_country["Germany"]) == 1

    grouped_with_agg = group_by(TEST_DATASET, ["country"], agg=len)
    assert grouped_with_agg["USA"] == 3
    assert grouped_with_agg["UK"] == 1

    mean_age_usa = get_mean_by_attribute(filtered_usa, "age")

    assert abs(mean_age_usa - 53.3333) < 0.001
