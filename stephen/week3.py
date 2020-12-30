from typing import List


def get_rainfall(data: List[tuple]) -> dict:

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
