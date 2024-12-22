"""
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, 
it is replaced by two stones. The left half of the digits are engraved on the new left stone,
and the right half of the digits are engraved on the new right stone.
(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's 
number multiplied by 2024 is engraved on the new stone.
"""

import sys


sys.set_int_max_str_digits(100000000)


def replace_leading_zeroes(stone: str) -> int:
    """
    replaces leading zeroes in a number
    """

    # while stone[0] == "0" and len(stone) > 1:
    #     stone = stone[1:]
    # return int(stone)
    return int(stone)


def solve(nums: list[int], blinks=75) -> int:
    """
    solves the problem for day 11
    """
    while blinks > 0:
        new_nums = []
        for stone in nums:
            if stone == 0:
                new_nums.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                half = len(stone) // 2
                first_half = int(stone[:half])
                second_half = replace_leading_zeroes(stone[half:])
                new_nums.append(first_half)
                new_nums.append(second_half)
            else:
                new_nums.append(stone * 2024)
        nums = new_nums
        blinks -= 1
    print(len(nums))


with open("input11.txt", "r", encoding="utf-8") as file:
    data = file.read().split(" ")
    int_input = []
    for i, n in enumerate(data):
        n = n.replace("\n", "").strip()
        int_input.append(int(n))

    solve(int_input)
# 814 1183689 0 1 766231 4091 93836 46
