from copy import deepcopy


def is_strictly_increasing(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True


def is_strictly_decreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            return False
    return True


def solve():
    safes = 0
    for line in open("input2.txt", "r"):
        line = line.strip().split()
        t = []
        for item in line:
            t.append(int(item))

        if is_strictly_increasing(t) or is_strictly_decreasing(t):
            good = True
            for i in range(1, len(t) - 1):
                diff1 = abs(t[i] - t[i - 1])
                diff2 = abs(t[i] - t[i + 1])
                if diff1 not in (1, 2, 3) or diff2 not in (1, 2, 3):
                    good = False
                    break
            if good:
                safes += 1
    print(safes)


def solve2():
    safes = 0
    for line in open("input2.txt", "r"):
        line = line.strip().split()
        t = []
        for item in line:
            t.append(int(item))

        arr = []
        for i in range(len(t) + 1):
            if i != len(t):
                arr = deepcopy(t)
                arr.pop(i)

            if is_strictly_increasing(arr) or is_strictly_decreasing(arr):
                good = True
                for i in range(1, len(arr) - 1):
                    diff1 = abs(arr[i] - arr[i - 1])
                    diff2 = abs(arr[i] - arr[i + 1])
                    if diff1 not in (1, 2, 3) or diff2 not in (1, 2, 3):
                        good = False
                        break
                if good:
                    safes += 1
                    break
    print(safes)


solve2()
