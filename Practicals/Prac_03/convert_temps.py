"""
Kazuki Pickersgill
Prac_03
CP1404 "convert temperature program"
"""

OUTPUT_FILE = "temps_output.txt"


def main():
    in_file = open("temps_input", "r")
    out_file = open(OUTPUT_FILE, "w")
    for fahrenheit in in_file:
        celsius = convert_to_celsius(float(fahrenheit))
        print(celsius, file=out_file)
    in_file.close()
    out_file.close()


def convert_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
