"""
CP1404
Kazuki Pickersgill
prac_08
Silver service taxi test
"""

from Practicals.prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
