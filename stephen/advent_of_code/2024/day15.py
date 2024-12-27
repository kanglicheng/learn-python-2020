"""
Solve the problem for Day 15.
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<

# from calendar import c
# from hmac import new
# from mimetypes import init
# from re import S
"""

from hmac import new


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))


def update_warehouse_map(
    current_row, current_col, new_row, new_col, warehouse_map, delta
):

    if warehouse_map[new_row][new_col] == "#":
        return current_row, current_col

    if warehouse_map[new_row][new_col] == ".":
        warehouse_map[current_row][current_col] = "."
        warehouse_map[new_row][new_col] = "@"
        return new_row, new_col

    if warehouse_map[new_row][new_col] == "O":
        found_space = False
        next_row, next_col = current_row + delta[0], current_col + delta[1]
        while warehouse_map[new_row][new_col] == "O":
            new_row, new_col = new_row + delta[0], new_col + delta[1]
            if warehouse_map[new_row][new_col] == ".":
                found_space = True
                break
            if warehouse_map[new_row][new_col] == "#":
                return current_row, current_col
        if found_space:
            warehouse_map[current_row][current_col] = "."
            warehouse_map[next_row][next_col] = "@"
            warehouse_map[new_row][new_col] = "O"
            return next_row, next_col


def solve_day15(initial_row, initial_col, warehouse_map, robot_moves):

    current_row, current_col = initial_row, initial_col
    delta = (0, 0)
    for move in robot_moves:
        if move == "v":
            new_row, new_col = current_row + 1, current_col
            delta = (1, 0)

        elif move == "^":
            new_row, new_col = current_row - 1, current_col
            delta = (-1, 0)
        elif move == ">":
            new_row, new_col = current_row, current_col + 1
            delta = (0, 1)
        elif move == "<":
            new_row, new_col = current_row, current_col - 1
            delta = (0, -1)
        else:
            raise ValueError(f"Invalid move {move}")

        ret = update_warehouse_map(
            current_row, current_col, new_row, new_col, warehouse_map, delta
        )

        if ret:
            current_row, current_col = ret

    print_matrix(warehouse_map)

    gps_total = 0
    for i, row in enumerate(warehouse_map):
        for j, ch in enumerate(row):
            if ch == "O":
                gps_total += 100 * i + j

    print(gps_total)


with open("input15.txt", "r") as f:
    data = f.read().strip().split("\n")
    mapping = [["" for _ in range(len(data[0]))] for _ in range(len(data))]
    moves, found_moves = "", False
    initial_row, initial_col = 0, 0
    for i, row in enumerate(data):
        if row == "":
            found_moves = True
            continue
        if found_moves:
            moves += row
            continue
        for j, ch in enumerate(row):
            if ch == "@":
                initial_row, initial_col = i, j
            mapping[i][j] = ch

    solve_day15(initial_row, initial_col, mapping, moves)
