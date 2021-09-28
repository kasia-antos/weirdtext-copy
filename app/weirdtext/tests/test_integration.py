from ..decoder import decode
from ..encoder import encode
import pytest


test_texts = [
    "",
    "$%*)",
    "This is a long looong test sentence,\nwith some big (biiiiig) words!",
    (
        "A wizard is never late, Frodo Baggins. Nor is he early. "
        "He arrives precisely when he means to."
    ),
    "Potatoes. Boil ’em, mash ’em, stick ’em in a stew.",
    "I can’t carry it for you, but I can carry you.",
    (
        "It’s like in the great stories, my Frodo. The ones that really "
        "mattered… and sometimes you didn’t want to know the end, because "
        "how could the end be happy? But, in the end, it’s only a passing "
        "thing, this shadow. Even darkness must pass."
    ),
]


@pytest.mark.parametrize("text", test_texts)
def test_encode_decode(text):
    encoded_text = encode(text)
    assert text == decode(encoded_text)
