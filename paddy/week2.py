def pig_latin():
    vowel = ["a", "e", "i", "o", "u"]
    inword = input("Please enter a word \n")
    if inword[0].lower() in vowel:
        print(inword+"way")

    else:
        temp = inword[1:len(inword)] + inword[0] + "ay"
        print(temp)


# pig_latin()

def ubbi_dubbi():
    vowel = ["a", "e", "i", "o", "u"]
    inword = input("Please enter a word \n")
    outword = ""
    for i in inword:
        if i in vowel:
            outword = outword + "ub" + i
        else:
            outword = outword + i
    print(outword)


ubbi_dubbi()
