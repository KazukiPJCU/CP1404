"""
CP1404/CP5632 - Practical
Shop Calculator
"""

total_cost = 0
number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    price = float(input("Price of item {}: ".format(i+1)))
    total_cost += price
if total_cost > 100:
    total_cost *= 0.9
print("Total price for {} items is ${:.2f}".format(number, total_cost))
