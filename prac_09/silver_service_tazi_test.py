"""
CP1404/CP5632 Practical
silver service taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Hummer", 0, 4)
    taxi.drive(10)
    print(taxi)
    print(f"Fare is ${taxi.get_fare():.2f}")


main()
