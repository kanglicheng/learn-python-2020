from typing import List, Tuple


def get_rainfall(data: List[Tuple[str, int]]) -> dict:

    totals = {}
    for pair in data:
        city, rain = pair[0], pair[1]
        if city in totals:
            totals[city] += rain
        else:
            totals[city] = rain

    return totals


# uses dict.get(key, defaultValue) method. If the city is not a key in totals,
# the default value of 0 will be returned.
def get_rainfall2(data: List[tuple]) -> dict:

    totals = {}
    for city, rain in data:
        totals[city] = totals.get(city, 0) + rain

    return totals


print(get_rainfall2([("boston", 10), ("sf", 5),
                     ("seattle", 20), ("sf", 3), ("boston", 5)]))


def take_order():
    MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}
    while True:
        print(MENU)
        order = input(
            "please order an item and amount (optional), i.e 'salad, 3' \n").split(", ")
        amount = 1
        item = order[0]
        if len(order) > 1:
            try:
                amount = int(order[1])
            except ValueError:
                print("amount not a number, please try again")
        if item in MENU:
            if MENU[item] >= amount:
                MENU[item] -= amount
            else:
                print("not enough {} left".format(item))
        else:
            print("item not sold here")


take_order()
