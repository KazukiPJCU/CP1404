"""
CP1404/CP5632 Practical
unreliable cat test
"""

from prac_09.unreliable_car import UnreliableCar


def main():

    reliable_car = UnreliableCar("Honda", 100, 100)
    unreliable_car = UnreliableCar("Great wall Ute", 100, 50)

    for i in range(1, 12):
        print(f"\nAttempting to drive {i}km:")
        print(f"{reliable_car.name:15} drove {reliable_car.drive(i):2}km")
        print(f"{unreliable_car.name:15} drove {unreliable_car.drive(i):2}km")

    print(reliable_car)
    print(unreliable_car)


main()
