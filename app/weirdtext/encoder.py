import random
from typing import List

from .utils import find_encodable_words


def shuffle(word: str) -> List[str]:
    """Shuffle letters in the word until the output is different than input.

    Please make sure that the such shuffling is possible to avoid infinite loops.

    Examples
    --------
    >>> shuffle("in")
    ['n', 'i']
    """
    letters = list(word)
    while True:
        random.shuffle(letters)
        new_word = "".join(letters)
        if new_word != word:
            return letters


def encode_word(word: str) -> List[str]:
    """Encode a word by shuffling inner letters.

    Examples
    --------
    >>> encode_word("ring")
    ['r', 'n', 'i', 'g']
    """
    inner_letters = word[1:-1]
    inner_letters = shuffle(inner_letters)
    return [word[0], *inner_letters, word[-1]]


def encode(text: str) -> str:
    r"""Encode text using Weirdtext encoder.

    Examples
    --------
    >>> encode("Lord of the Ring(s)")
    '\n—weird—\nLrod of the Rnig(s)\n—weird—\nLord Ring'
    """
    encodable_words, words_span = find_encodable_words(text)
    letters = list(text)

    for word, word_span in zip(encodable_words, words_span):
        left_pos, right_pos = word_span
        letters[left_pos:right_pos] = encode_word(word)

    encoded_words = sorted(encodable_words, key=str.casefold)
    encoded_text = (
        "\n—weird—\n" + "".join(letters) + "\n—weird—\n" + " ".join(encoded_words)
    )

    return encoded_text
