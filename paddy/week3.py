# 1
def get_rainfall(lst):
    dct = {}
    for item in lst:
        if item[1] not in dct:
            dct.update(dict([item]))
        else:
            dct[item] += item[1]
    return dct


# print(get_rainfall([("boston", 10), ("sf", 5),
#                     ("seattle", 20), ("sf", 3), ("boston", 5)]))


# 2

def take_order():
    menu = {'sandwich': 10, 'tea': 7, 'salad': 9}

    while True:
        print(menu)
        item = input("What do you want to order? \n")
        if item in menu and menu[item] > 0:
            menu[item] -= 1
            print("OK")
        else:
            print("item not available")


# take_order()

# 3
def most_repeat(lst):
    maxrep = 1
    final = lst[0]
    for item in lst:
        dct = {}
        for i in item:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        if max(dct.values()) > maxrep:
            maxrep = max(dct.values())
            final = item
    return final


#print(most_repeat(['this', 'is', 'an', 'elementary', 'test', 'example']))

# 4
def how_many_different(lst):
    dct = {}
    for item in lst:
        dct[item] = dct.get(item, 0) + 1
    return len(dct)


# a = how_many_different([1, 2, 1, 1, 3])
# print(a)
