"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730316345"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
randNum = randint(1, 100)
if randNum < 30:
    print("A beautiful, smart and loving person will be coming into your life.")
else: 
    if randNum < 70:
        print("Your life will be happy and peaceful.")
    elif randNum <90:
        print("Soon life will become more interesting.")
    elif randNum <100:
        print("Beware the snakes in the grass.")
print("Now, go spread positive vibes!")