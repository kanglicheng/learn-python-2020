"""
Chooses a random integer in [0, 100]. Asks user to enter a guess,
terminates only when user guesses correctly
"""
import random


def guessing_game():
    number = random.randint(1, 5)
    while True:
        guess = int(
            input("Please enter a number between 1 and 5 (inclusive) "))
        if guess == number:
            return "correct!"


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


#print(mysum(1, 2, 3, 4, 5))


def get_avg():
    # taking number from user enter number through string message
    # stores them in an array and then averages values in array5
    total = 0
    count = 0
    while True:

        user_input = input("enter a number: ")
        try:
            n = int(user_input)
            count += 1
        except:
            break
        total += n
    if count > 0:
        print(total/count)
    return


get_avg()
