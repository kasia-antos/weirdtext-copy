from ..encoder import encode, shuffle, encode_word
import pytest


def test_shuffle():
    word = "wizard"
    test_value = sorted(shuffle(word))
    expected = ["a", "d", "i", "r", "w", "z"]
    assert test_value == expected


def test_encode_word():
    word = "wizard"
    test_value = encode_word(word)
    assert test_value[0] == "w"
    assert test_value[-1] == "d"
    test_value = sorted(test_value[1:-1])
    expected = ["a", "i", "r", "z"]
    assert test_value == expected


test_texts = [
    ("", "\n—weird—\n\n—weird—\n"),
    (
        "Heeey, what's up? ~ Kate",
        "\n—weird—\nHeeey, waht's up? ~ Ktae\n—weird—\nKate what",
    ),
]


@pytest.mark.parametrize("text,expected", test_texts)
def test_encode(text, expected):
    test_value = encode(text)
    assert test_value == expected
