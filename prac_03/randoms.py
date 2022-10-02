import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
#   7
#   Smallest = 5    Largest = 20
#
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
#   9
#   Smallest = 3    Largest = 9
#   No, it's in increments of 2
#
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
#   3.6577418513714477
#   Smallest = 2.5  Largest = 5.5
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
