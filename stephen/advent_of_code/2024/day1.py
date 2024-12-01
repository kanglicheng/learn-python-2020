from collections import Counter


def solve():
    l1, l2 = [], []
    for line in open("input1.txt", "r"):
        line = line.strip().split()
        l1.append(int(line[0]))
        l2.append(int(line[-1]))

    l1.sort()
    l2.sort()
    total_dist = 0
    for x, y in zip(l1, l2):
        total_dist += abs(x - y)

    print(total_dist)


def solve2():
    l1, l2 = [], []
    for line in open("input1.txt", "r"):
        line = line.strip().split()
        l1.append(int(line[0]))
        l2.append(int(line[-1]))

    l2_count = Counter(l2)
    total_score = 0
    for n in l1:
        total_score += l2_count[n] * n

    print(total_score)


solve2()
