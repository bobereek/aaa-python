from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch
import json


class TestWhatIsYearNow(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_ymd_format(self, mock_urlopen):
        mock_response = mock_urlopen.return_value
        mock_response.__enter__ = lambda _: mock_response
        mock_response.__exit__ = lambda *_: None

        mock_response.read.return_value = json.dumps({"currentDateTime": "2025-11-10"}).encode("utf-8")

        result = what_is_year_now()

        self.assertEqual(result, 2025)

    @patch("urllib.request.urlopen")
    def test_dmy_format(self, mock_urlopen):
        mock_response = mock_urlopen.return_value
        mock_response.__enter__ = lambda _: mock_response
        mock_response.__exit__ = lambda *_: None

        mock_response.read.return_value = json.dumps({"currentDateTime": "10.11.2025"}).encode("utf-8")

        year = what_is_year_now()
        self.assertEqual(year, 2025)

    @patch("urllib.request.urlopen")
    def test_invalid_format(self, mock_urlopen):
        mock_response = mock_urlopen.return_value
        mock_response.__enter__ = lambda _: mock_response
        mock_response.__exit__ = lambda *_: None

        mock_response.read.return_value = json.dumps({"currentDateTime": "10/11/2025"}).encode("utf-8")

        with self.assertRaises(ValueError) as cm:
            what_is_year_now()
        self.assertEqual(str(cm.exception), "Invalid format")

    @patch("urllib.request.urlopen", side_effect=Exception("Network error"))
    def test_network_error(self, mock_urlopen):
        with self.assertRaises(Exception) as cm:
            what_is_year_now()
        self.assertEqual(str(cm.exception), "Network error")

    @patch("urllib.request.urlopen")
    def test_missing_field(self, mock_urlopen):
        # Мокируем ответ без поля currentDateTime
        mock_response = mock_urlopen.return_value
        mock_response.__enter__ = lambda _: mock_response
        mock_response.__exit__ = lambda *_: None

        mock_response.read.return_value = json.dumps({}).encode("utf-8")

        with self.assertRaises(KeyError):
            what_is_year_now()
