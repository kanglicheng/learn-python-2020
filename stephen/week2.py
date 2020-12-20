def pig_latin(word):
    vowels = "aeiou"
    if not word:
        return None
    if word[0] in vowels:
        return word+"way"
    else:
        new_word = [word[1:]+word[0]+"ay"]
        return "".join(new_word)


print(pig_latin("python"))
print(pig_latin("computer"))
print(pig_latin(("air")))
