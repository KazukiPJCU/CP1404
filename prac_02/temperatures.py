"""
CP1404/CP5632 - Practical 2
Temperature
"""


# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = (fahrenheit - 32) * 5 / 9
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")
#

def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(convert_celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            print("Result: {:.2f} C".format(convert_fahrenheit_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
