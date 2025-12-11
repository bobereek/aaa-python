# полный код в файле morse.py
from morse import decode
import pytest


@pytest.mark.parametrize(
    "morse_message, expected",
    [
        ("... --- ...", "SOS"),
        (".... . .-.. .-.. ---", "HELLO"),
        (".-- --- .-. .-.. -..", "WORLD"),
        (".- .- .-", "AAA"),
        ("", ""),
        (".-", "A"),
    ],
)
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected
