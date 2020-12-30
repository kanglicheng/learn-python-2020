from collections import Counter
from distutils.archive_util import make_zipfile
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


def most_repeating_chars(words):
    max_count = 1
    most_frequent = words[0]
    for word in words:
        counts = Counter(word)
        if max(counts.values()) > max_count:
            max_count = max(counts.values())
            most_frequent = word
    return most_frequent


# returns the most frequently appearing word in words


def most_frequent(words):
    word_dict = {}
    most_frequent = words[0]
    max_count = 1
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
        if word_dict[word] > max_count:
            max_count = word_dict[word]
            most_frequent = word
    return most_frequent


print(most_repeating_chars(
    ['this', 'is', 'an', 'elementary', 'test', 'example']))
