"""
CP1404/CP5632 - Practical 2
Score Menu
"""


def main():
    """Get a numeric score and display its status."""
    MENU = """Get a numeric score and display its status\nQ - Quiet\nE - Enter Number"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            number = float(input("Score: "))
            print("Result: {}".format((determine_score(number))))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
