"""Part 2 of dictionary assignment"""

__author__ = "730662835"

from dictionary import invert, count, favorite_color, bin_len
import pytest


def test_invert() -> None:
    """Testing the Invert Function"""
    assert invert({"1": "a", "2": "b"}) == {"a": "1", "b": "2"}

    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count() -> None:
    """Testing Count"""
    assert count(
        [
            "d",
            "a",
        ]
    ) == {"d": 1, "a": 1}


def test_favorite_color() -> None:
    """Testing Favorite Color"""
    assert favorite_color({"a": "blue", "b": "green", "c": "blue"}) == "blue"


def test_bin_len() -> None:
    """Testing Bin Length"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
