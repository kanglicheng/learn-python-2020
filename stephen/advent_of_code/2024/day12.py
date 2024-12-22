"""
Advent of Code Day 12 Solution
This module contains functions to solve the puzzle for Day 12 of the Advent of Code event.
For each region in the matrix, indicated by a letter, calculate the area 
and the perimter of the region.
Then sum up the area multiplied by the perimeter for each region.
"""

from collections import defaultdict
import random

# from email.policy import default
# pydocs


def solve_day_12(matrix: list[list[str]]) -> int:
    """
    Solves the Day 12 puzzle using the provided matrix of string elements.

    Args:
        matrix (list[list[str]]): A nested list of string elements representing puzzle data.

    Returns:
        int: The result of solving the Day 12 puzzle, calculated from the input matrix.
    """

    def bfs(matrix, i, j, ch, visited):
        area = 0
        perimeter = 0
        queue = [(i, j)]
        visited.add((i, j))
        while queue:
            x, y = queue.pop(0)
            area += 1
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < len(matrix)
                    and 0 <= ny < len(matrix[0])
                    and matrix[nx][ny] == ch
                ):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                else:
                    perimeter += 1
        return area, perimeter

    visited = set()
    symbol_to_data = defaultdict(dict)
    for i, row in enumerate(matrix):
        for j, ch in enumerate(row):
            if ch not in symbol_to_data:
                if (i, j) not in visited:
                    area, perimeter = bfs(matrix, i, j, ch, visited)
                    symbol_to_data[ch] = {"area": area, "perimeter": perimeter}
            else:
                if (i, j) not in visited:
                    area, perimeter = bfs(matrix, i, j, ch, visited)
                    while ch in symbol_to_data:
                        ch = ch + str(random.randint(0, 10))
                    symbol_to_data[ch] = {"area": area, "perimeter": perimeter}

    result = sum(data["area"] * data["perimeter"] for data in symbol_to_data.values())
    print(result)


with open("input12.txt", "r", encoding="utf-8") as file:
    data = [list(line.strip()) for line in file]
    solve_day_12(data)


# It contains:

# A region of R plants with price 12 * 18 = 216.
# A region of I plants with price 4 * 8 = 32.
# A region of C plants with price 14 * 28 = 392.
# A region of F plants with price 10 * 18 = 180.
# A region of V plants with price 13 * 20 = 260.
# A region of J plants with price 11 * 20 = 220.
# A region of C plants with price 1 * 4 = 4.
# A region of E plants with price 13 * 18 = 234.
# A region of I plants with price 14 * 22 = 308.
# A region of M plants with price 5 * 12 = 60.
# A region of S plants with price 3 * 8 = 24.
