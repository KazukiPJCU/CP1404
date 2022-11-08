""" My Guitars
 Estimated Time:   30
 Actual Time:      36   """

from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitar file, add guitars, display guitars, save guitars to file."""
    guitars = load_guitars()
    get_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars)


def save_guitars(guitars):
    """Save guitars to file."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display guitars."""
    print("\nGuitars:")
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    """Add new user guitars to guitars list."""
    name = input("Name: ")
    while name != "":
        year = valid_input("Year: ", int)
        cost = valid_input("Cost: ", float)
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar)
        print("Added to guitars")
        name = input("Name: ")


def load_guitars():
    """Load guitars."""
    guitars = []
    with open(FILENAME) as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
            # print(guitar) #Checking guitar are correctly formatted
    return guitars


def valid_input(user_input, input_type):
    """Check if valid input."""
    is_valid = False
    while not is_valid:
        try:
            typed_input = input_type(input(user_input))
            if typed_input < 0:
                print("Must be >= 0")
            else:
                is_valid = True
        except ValueError:
            print("Must be a number")
    return typed_input


main()
