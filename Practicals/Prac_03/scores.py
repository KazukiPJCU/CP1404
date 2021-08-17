"""
Kazuki pickersgill
"""

import random


def main():
    number_of_scores = get_number_of_random_scores()
    repeats = 0
    while repeats < number_of_scores:
        repeats += 1
        random_score = get_random_score()
        result = get_result(random_score)
        # print(random_score, "is", result)
        print("{} is {}".format(random_score, result))


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_number_of_random_scores():
    number_of_scores = int(input("Number of random scores: "))
    return number_of_scores


def get_random_score():
    random_number = random.randint(0, 100)
    return random_number


def get_score():
    score = float(input("Enter score: "))
    return score


main()
