"""CP1404/CP5632 Practical -  Guitars.
Time 30 min
"""
from prac_06.guitar import Guitar


def main():
    """Guitar program"""
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Gibson L-5 CES", 1922, 16035.40)]
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar.name:<20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars")


main()
