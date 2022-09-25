"""
CP1404/CP5632 - Practical 2
Password checker
"""

min_length = 5


def main():
    password = get_password(min_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter password at least {} characters: ".format(min_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password at least {} characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()