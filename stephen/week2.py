def pig_latin(word):
    vowels = "aeiou"
    if not word:
        return None
    if word[0] in vowels:
        return word+"way"
    else:
        new_word = [word[1:]+word[0]+"ay"]
        return "".join(new_word)


# print(pig_latin("Python"))
# print(pig_latin("computer"))
# print(pig_latin(("air")))


def ubbi_dubbi():
    word = input("please enter a word: ")
    vowels = "aeiou"
    result = []
    for c in word:
        if c in vowels:
            result.append("ub")
        result.append(c)
    return "".join(result)


# print(ubbi_dubbi())


def get_running_avg():
    numbers = input("enter the numbers: ")
    numbers = numbers.split(" ")
    array = [int(n) for n in numbers]
    print(array)


get_running_avg()
