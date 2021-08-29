"""
CP1404
Kazuki Pickersgill
prac_04
"""
numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. What values do the following expressions have?
# 2. Without running the code, write down your answers to these questions
# 3,2,1,3-1-4-1-5-9,1,true,false,false,3-1-4-1-5-9-2-6-5-3
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]


# Write Python expressions (in your Python file) to achieve the following:

# Change the first element of numbers to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Get all the elements from numbers except the first two
numbers[2:]
# Check if 9 is an element of numbers
9 in numbers