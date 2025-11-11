# полный код в файле morse.py
from morse import LETTER_TO_MORSE


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'

    >>> encode('HELLO')
    '.... . .-.. .-.. ---'

    >>> encode(1)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable

    >>> encode('Hello')
    Traceback (most recent call last):
        ...
    KeyError: 'e'
    """
    encoded_signs = [LETTER_TO_MORSE[letter] for letter in message]

    return " ".join(encoded_signs)
