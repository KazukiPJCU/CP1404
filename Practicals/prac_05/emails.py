"""
CP1404/CP5632 Practical
Email & name dictionary
Kazuki Pickersgill
"""

"""Create dictionary of emails and corresponding names."""
email_to_name = {}
email = input("Email: ")
while email != "":
    remove_email = email.split('@')[0]
    parts = remove_email.split('.')
    name = " ".join(parts).title()
    confirmation = input("Is your name {}? (Y/N) ".format(name))
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print("{} ({})".format(name, email))
