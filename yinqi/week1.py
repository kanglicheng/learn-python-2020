"""
Chooses a random integer in [0, 100]. Asks user to enter a guess,
terminates only when user guesses correctly
"""
import random
import numpy as np

def guessing_game():
    number = random.randint(0, 100)
    while True:
        guess = int(input("Please enter a number between 1 and 100 (inclusive)"))
        if guess == number:
            return "correct!"
        elif guess > number:
            print("too large!") 
        else:
            print("too small!")   

# print(guessing_game())


"""
implement sum function
sum(a, b, c, d, ... m, n) = a+b+c+d+...+m+n
"""


def mysum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def newaverage():
    numbers = int(input("Please input a number: "))
    while True:
        new = input("Please input another number (Enter K/k to stop): ")
        if new.upper() == "K":
            mean = sum(numbers) / len(numbers)
            return print("The average of your list is " + str(mean))
        else:
            numbers = np.append(numbers, int(new))

newaverage()
