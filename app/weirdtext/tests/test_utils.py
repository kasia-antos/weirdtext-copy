from ..utils import find_words, is_encodable, find_encodable_words


def test_find_words():
    text = "It’s mine, my own, my love, my precious."
    words = find_words(text)
    test_value = [word.group() for word in words]
    expected = ["It", "s", "mine", "my", "own", "my", "love", "my", "precious"]
    assert test_value == expected


def test_is_encodable():
    assert not is_encodable("p")
    assert is_encodable("Gandalf")
    assert not is_encodable("Yeeeeey")


def test_find_encodable_words():
    test_value = find_encodable_words("Nobody tosses a Dwarf!")
    expected = (["Nobody", "tosses", "Dwarf"], [(0, 6), (7, 13), (16, 21)])
    assert test_value == expected