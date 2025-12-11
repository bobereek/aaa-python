# полный код в файле one_hot_encoder.py
from one_hot_encoder import fit_transform
import unittest


class test_fit_tranform(unittest.TestCase):
    def test_basic(self):
        result = fit_transform(["a", "b", "c", "d"])
        expected = [
            ("a", [0, 0, 0, 1]),
            ("b", [0, 0, 1, 0]),
            ("c", [0, 1, 0, 0]),
            ("d", [1, 0, 0, 0]),
        ]
        self.assertEqual(result, expected)

    def test_empty(self):
        self.assertEqual(fit_transform([]), [])

    def test_single_element(self):
        result = fit_transform(["x"])
        self.assertEqual(result, [("x", [1])])

    def test_duplicates(self):
        result = fit_transform(["a", "a", "b"])
        expected = [
            ("a", [0, 1]),
            ("a", [0, 1]),
            ("b", [1, 0]),
        ]
        self.assertEqual(result, expected)

    def test_exception_no_args(self):
        self.assertRaises(TypeError, fit_transform)

    def test_string_input(self):
        result = fit_transform("abc", "bca", "cab")
        expected = [
            ("abc", [0, 0, 1]),
            ("bca", [0, 1, 0]),
            ("cab", [1, 0, 0]),
        ]
        self.assertEqual(result, expected)
