from hmac import new
from mimetypes import init
import re
import time

initial_ls = []
vel_ls = []
data = open("input14.txt", "r").read().strip()
for line in data.strip().split("\n"):
    initial = re.findall(r"p=(\d+),(\d+)", line)
    initial_ls.append([int(initial[0][0]), int(initial[0][1])])
    vel = re.findall(r"v=([-]?\d+),([-]?\d+)", line)
    vel_ls.append([int(vel[0][0]), int(vel[0][1])])


def pretty_print(grid):
    for row in grid:
        new_str = ""
        for ch in row:
            new_str += "#" if ch == 1 else "."
        print(new_str)


WIDTH = 101
HEIGHT = 103
c1, c2, c3, c4 = 0, 0, 0, 0

robots = []
ROUNDS = 10000


ROUNDS_1 = 100

# Part 1

for index in range(len(initial_ls)):
    start_po = initial_ls[index]
    vel = vel_ls[index]
    for i in range(ROUNDS_1):
        start_po[0] = (start_po[0] + vel[0]) % WIDTH
        start_po[1] = (start_po[1] + vel[1]) % HEIGHT

    robots.append(start_po)


midx, midy = WIDTH // 2, HEIGHT // 2
q1 = q2 = q3 = q4 = 0
for x, y in robots:
    if x == midx or y == midy:
        continue
    if x < midx and y < midy:
        q1 += 1
    elif x > midx and y < midy:
        q2 += 1
    elif x < midx and y > midy:
        q3 += 1
    elif x > midx and y > midy:
        q4 += 1

print(q1 * q2 * q3 * q4)

# Part 2
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

for rn in range(ROUNDS):

    for idx, (col, row) in enumerate(initial_ls):

        grid[row][col] = 0
        new_col, new_row = (col + vel_ls[idx][0]) % WIDTH, (
            row + vel_ls[idx][1]
        ) % HEIGHT
        initial_ls[idx] = [new_col, new_row]
        grid[new_row][new_col] = 1

    for row in grid:
        new_str = ""
        for ch in row:
            new_str += "#" if ch == 1 else "."
            if "#######" in new_str:
                pretty_print(grid)
                print("Round", rn + 1)
                time.sleep(1)
                break
