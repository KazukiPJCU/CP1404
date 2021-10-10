"""
CP1404
Kazuki Pickersgill
prac_08
unreliable car test
"""

from Practicals.prac_08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""

    good_car = UnreliableCar("Mostly reliable car,", 100, 90)
    bad_car = UnreliableCar("Unreliable car", 100, 9)

    for i in range(1, 12):
        print("Attempted to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(good_car)
    print(bad_car)


main()
