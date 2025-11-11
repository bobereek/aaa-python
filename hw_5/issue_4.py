# полный код в файле one_hot_encoder.py
import pytest
from one_hot_encoder import fit_transform


def test_basic():
    result = fit_transform(["a", "b", "c", "d"])
    expected = [
        ("a", [0, 0, 0, 1]),
        ("b", [0, 0, 1, 0]),
        ("c", [0, 1, 0, 0]),
        ("d", [1, 0, 0, 0]),
    ]
    assert result == expected


def test_empty():
    assert fit_transform([]) == []


def test_single_element():
    result = fit_transform(["x"])
    assert result == [("x", [1])]


def test_duplicates():
    result = fit_transform(["a", "a", "b"])
    expected = [
        ("a", [0, 1]),
        ("a", [0, 1]),
        ("b", [1, 0]),
    ]
    assert result == expected


def test_exception_no_args():
    with pytest.raises(TypeError):
        fit_transform()


def test_string_input():
    result = fit_transform("abc", "bca", "cab")
    expected = [
        ("abc", [0, 0, 1]),
        ("bca", [0, 1, 0]),
        ("cab", [1, 0, 0]),
    ]
    assert result == expected
