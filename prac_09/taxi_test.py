"""
CP1404/CP5632 Practical
Taxi test
"""

from taxi import Taxi


def main():
    """taxi test"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
