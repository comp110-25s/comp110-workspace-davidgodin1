"""Let's Play Wordle"""

__author__ = "730662835"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 0
    max_turns = 6

    while turn <= max_turns - 1:
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")
        user_guess = input_guess(len(secret))
        result = emojified(user_guess, secret)
        print(result)

        if user_guess == secret:
            print(f"You won in {turn}/{max_turns} turns!")
            return

    print(f"X/{max_turns} - Sorry, try again tomorrow!")


def contains_char(word: str, singlecharacter: str) -> bool:
    """Looking for characters in word"""
    assert len(singlecharacter) == 1, f"len('{singlecharacter}') is not 1"
    i = 0
    while i <= len(word) - 1:
        if singlecharacter == word[i]:
            return True
        else:
            i = i + 1

    return False


def emojified(guess: str, secret: str) -> str:
    """testing for placement"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i = 0
    result = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(singlecharacter=guess[i], word=secret):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

        i += 1
    return result


def input_guess(N: int) -> str:
    var1 = input(f"Enter a {N} character word:")
    while len(var1) != N:
        var1 = input(f"That wasn't {N} chars! Try again:")
    return var1
