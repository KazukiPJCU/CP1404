"""
CP1404/CP5632 - Practical 2
Score
"""


def main():

    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        score = float(input("Enter a valid score: "))
    print(grade(score))


def grade(score):
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
