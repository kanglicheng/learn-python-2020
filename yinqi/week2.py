'''''
week 2: pig latin
'''''
def pig_latin():
    vowel = ["a", "e", "i", "o", "u"]
    word = input("Please input a word: ")
    first = word[0]
    if first.lower() in vowel:
        return(print(word + "way"))
    else:
        return(print(word[1:len(word)] + word[0] + "ay"))

# pig_latin()

def ubbi_dubbi():
    vowel = ["a", "e", "i", "o", "u"]
    word = input("Please input a word: ")
    output = []
    for i in range(len(word)):
        if word[i] in vowel:
            output += ["ub" + word[i]]
        else:
            output += [word[i]]
    final = "".join(output)
    return(print(final))

ubbi_dubbi()