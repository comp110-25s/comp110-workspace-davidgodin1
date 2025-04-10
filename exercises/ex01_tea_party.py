"""Creating a lovely tea party"""

__DavidGodin__: str = "730662835"


def main_planner(guests: int) -> None:
    """entrypoint of your program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=(tea_bags(people=guests)), treat_count=(treats(people=guests))
            )
        )
    )


def tea_bags(people: int) -> int:
    """Number of Tea Bags"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats"""
    return int(1.5 * (tea_bags(people=people)))


def cost(tea_count: int, treat_count: int) -> float:
    """How much the tea party costs"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
