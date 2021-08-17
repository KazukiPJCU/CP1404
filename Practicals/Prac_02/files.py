# Question 1: Ask name write to file
# OUTPUT_FILE = "name.txt"
# out_file = open(OUTPUT_FILE, "w")
# name = input("Enter Name: ")
# print(name,file=out_file)
# out_file.close()
#
# # Question 2: Open name.txt prints name
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# print("Your Name is", name)
# in_file.close()

# Question 3:
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
