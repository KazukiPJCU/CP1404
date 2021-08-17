"""
Kazuki Pickersgill
CP1404 "Broken Score"
"""
import random


def main():
    score = get_score()
    result = get_result(score)
    print(result)
    random_score = get_random_score()
    result = get_result(random_score)
    print(result)


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score():
    random_number = random.randint(0, 100)
    return random_number


def get_score():
    score = float(input("Enter score: "))
    return score


main()
