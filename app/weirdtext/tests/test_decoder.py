from ..decoder import (
    sort_inside,
    raise_if_true,
    create_mapper,
    decode,
    DecodingError,
)
import pytest


def test_raise_if_true():
    msg = "Input text has invalid format. Are you sure you used the right encoder?"

    with pytest.raises(ValueError, match=msg):
        raise_if_true(True)

    raise_if_true(False)


def test_sort_inside():
    test_input = sort_inside("Pippin")
    expected = "Piippn"
    assert test_input == expected


def test_create_mapper():
    words = ["Elrond", "Arwena", "Galadriela"]
    test_input = create_mapper(words)
    assert len(test_input) == 3
    assert test_input["Elnord"] == "Elrond"
    assert test_input["Aenrwa"] == "Arwena"
    assert test_input["Gaadeillra"] == "Galadriela"


def test_create_mapper_invalid():
    words = ["Elrond", "Elornd"]
    with pytest.raises(DecodingError, match="Input words are ambigious"):
        create_mapper(words)


test_texts = [
    ("\n—weird—\n\n—weird—\n", ""),
    ("\n—weird—\nHi\n—weird—\n", "Hi"),
    (
        "\n—weird—\nHeeey, waht's up? ~ Ktae\n—weird—\nKate what",
        "Heeey, what's up? ~ Kate",
    ),
]


@pytest.mark.parametrize("text,expected", test_texts)
def test_decode(text, expected):
    test_value = decode(text)
    assert test_value == expected


test_texts = [
    "",
    "\n—weird—\n",
    "\n—weird—\n\n—weird—\nKate",
    "\n—weird—\nKtae\n—weird—\n",
    "random\n—weird—\nKtae\n—weird—\nKate",
]


@pytest.mark.parametrize("text", test_texts)
def test_decode_invalid(text):
    with pytest.raises(ValueError):
        decode(text)
