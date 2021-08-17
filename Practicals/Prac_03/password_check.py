""""
Kazuki Pickersgill

Password checker handwritten code
"""

MIN_LENGTH = 5
password = input("Type in password: ")
while len(password) < MIN_LENGTH:
    print("Password to short", {}).format(MIN_LENGTH)
    password = input("Type in password: ")
for characters in password:
    print("*", end="")
