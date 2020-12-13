import random

def play_game():
    number = random.randint(1,10)
    while True:
        guess = int(input("Please enter a number btw 1 and 10 \n"))
        if guess == number:
            print("Nice guess")
            return
        elif guess > number:
            print("too large")
        else :
            print("too small")
play_game()