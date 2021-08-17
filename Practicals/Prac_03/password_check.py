""""
Kazuki Pickersgill

Password checker handwritten code
"""

MIN_LENGTH = 5


def main():
    password = get_password()
    while len(password) < MIN_LENGTH:
        print("Password to short, {} is the minimum password length".format(MIN_LENGTH))
        password = get_password()
    print_asterick_password(password)


def print_asterick_password(password):
    for characters in password:
        print("*", end="")


def get_password():
    password = input("Type in password: ")
    return password


main()
