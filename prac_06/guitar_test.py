"""CP1404/CP5632 Practical -  Guitar Test."""
import datetime
from prac_06.guitar import Guitar

date = datetime.datetime.now()

CURRENT_YEAR = date.year


def run_tests():
    """Tests Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    run_tests()