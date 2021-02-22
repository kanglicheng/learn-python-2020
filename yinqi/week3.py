# examples of dictionary
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print(Dict)	
# del Dict ['Charlie']
# print(Dict)

# t = "Tim" in Dict
# print(t)

# res = {}
# print("x" in res)

"""""""""
problem 1
"""""""""

def get_rainfall(dat):
    res = {}
    for x in dat:
        city = x[0]
        amount = x[1]
        # print(type(city))
        # print(type(amount))
        if city in res:
            res[city] += amount
        else:
            res.update(dict([x]))
            # res[city] = amount
    return res


# x = get_rainfall([("boston", 10), ("sf", 5), ("seattle", 20), ("sf", 3), ("boston", 5)])
# print(x)

# The input of update of dictionary should be an object of length 2, therefore a Tuple of Tuple is allowed but a singe tuple is not, since the element of a simple tuple is "str" or "int"
# y = (("boston", 10), ("sf", 5), ("seattle", 20), ("boston", 5))
# print(dict(y))
# {"a":1}

"""""""""
problem 2
"""""""""
menu = {'sandwich': 10, 'tea': 7, 'salad': 9}

def take_order():
    ind = True
    while ind:
        order = input()
        if order not in ["sandwich", "tea", "salad"]:
            print("available on the menu: sandwich, tea, salad")
        elif menu[order] > 0:
            menu[order] -= 1
            print("OK, stock = " + str(menu[order]))
        else:
            print("Item not available")
        if menu["sandwich"] == menu["tea"] == menu["salad"] == 0:
            ind = False

# take_order()



"""""""""""
Problem 3
"""""""""""
def most_repeating(words):
    res_count = 0
    res_word = ""
    for i in range(len(words)):
        x = words[i]
        count = {}
        for j in x:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
        p = max(count.values())
        if p > res_count:
            res_count = p
            res_word = x
    print(res_word + " is the most repeated word in the list, the most repeated number is " + str(res_count))


# words = ['this', 'is', 'an', 'elementary', 'test', 'example']
# most_repeating(words)
            

"""""""""""
Problem 4
"""""""""""
def how_many_different(dat):
    res = {}
    for x in dat:
        if x in res:
            res[x] += 1
        else:
            res[x] = 1
    unique = res.keys()
    return len(unique)

print(how_many_different([1, 2, 1, 1, 3, 1, 1, 6]))
