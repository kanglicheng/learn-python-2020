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
#play_game()



def multiply_all(list):
    pdt = 1
    for i in list:
        pdt = pdt * i
    print(pdt)
    return

#multiply_all([2,9,10])
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
print(len(str1))