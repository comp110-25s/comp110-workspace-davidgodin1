"""Dictionary Assignment"""

__author__ = "730662835"


def invert(switch: dict[str, str]) -> dict[str, str]:

    d: dict[str, str] = {}

    for key, value in switch.items():
        if value in d:
            raise KeyError("Duplicate key found")
        d[value] = key

    return d


def count(number: list[str]) -> dict[str, int]:
    d2: dict[str, int] = {}
    i = 0
    while i < len(number):
        item = number[i]

        if item in d2:
            d2[item] += 1

        else:
            d2[item] = 1

        i += 1

    return d2


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most common color in the dictionary"""
    d3: dict[str, int] = {}
    for name in colors:
        if colors[name] in d3:
            d3[colors[name]] += 1
        else:
            d3[colors[name]] = 1

    max_count = 0
    max_color = ""
    for color, count in d3.items():
        if count > max_count:
            max_count = count
            max_color = color

    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Returns a dictionary with the length of words as keys and sets of words"""
    d4: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in d4:
            d4[length].add(word)
        else:
            d4[length] = {word}
    return d4
