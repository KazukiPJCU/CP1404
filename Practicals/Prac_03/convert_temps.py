"""
Kazuki Pickersgill
Prac_03
CP1404 "convert temperature program"
"""

OUTPUT_FILE = "temps_output.txt"


def main():
    in_file = open("temps_input", "r")
    out_file = open(OUTPUT_FILE, "w")
    for lines in in_file:
        celsius = get_celsius(float(lines))
        print(celsius, file=out_file)
    in_file.close()
    out_file.close()


def get_celsius(lines):
    celsius = 5 / 9 * (lines - 32)
    return celsius


main()
