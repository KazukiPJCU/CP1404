"""CP1401
Quick Picks
"""

import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    if number_of_quick_picks == 0:
        quit_program()
    while number_of_quick_picks < 0:
        print("Please type in number greater than 0")
        number_of_quick_picks = int(input("How many quick picks? "))
        if number_of_quick_picks == 0:
            quit_program()

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def quit_program():
    print("Program exited have a nice day!")
    quit()


main()
