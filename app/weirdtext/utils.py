import re
from typing import Iterable, List, Tuple

WordSpan = Tuple[int, int]


def find_words(text: str) -> Iterable[re.Match]:
    """Find words in given string."""
    tokenize_re = re.compile(r"(\w+)", re.U)
    words = tokenize_re.finditer(text)
    return words


def is_encodable(word: str) -> bool:
    """Check if the word can be encoded.

    Examples
    --------
    >>> is_encodable("OK")
    False
    >>> is_encodable("Frodo")
    True
    """
    if len(word) <= 3:
        return False
    word = word[1:-1]
    single_letters_count = len(set(word))
    if single_letters_count < 2:
        return False
    return True


def find_encodable_words(text: str) -> Tuple[List[str], List[WordSpan]]:
    """Find words that can be encoded in the given text.

    Returns a list of encodable words and a list of word position
    in the input text in the format (start_position, end_position).

    Examples
    --------
    >>> find_encodable_words("You shall not pass!")
    (['shall', 'pass'], [(4, 9), (14, 18)])
    """
    words = find_words(text)
    encodable_words = []
    span = []
    for word_match in words:
        word = word_match.group()

        if is_encodable(word):
            encodable_words.append(word)
            span.append(word_match.span())

    return encodable_words, span
