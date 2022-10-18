"""
CP1404/CP5632 Practical
Emails
Estimate: 40
Actual: 38
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        Confirm = input(f"Is your name {name}? (Y/n) ")
        if Confirm.upper() != "Y" and Confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print("{} is the name for the email {}".format(name, email))


def get_name(email):
    asperand = email.split('@')[0]
    parts = asperand.split('.')
    name = " ".join(parts).title()
    return name


main()
