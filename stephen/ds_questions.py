def get_contribution(r, c, matrix):
    total = 0
    m, n = len(matrix), len(matrix[0])
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_row = d[0] + r
        new_col = d[1] + c
        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
            total += 1
        else:
            if matrix[new_row][new_col] == 0:
                total += 1
    return total


def river_perimeter(matrix):
    perimeter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                perimeter += get_contribution(i, j, matrix)
    return perimeter


print(river_perimeter([[1, 0]]))
print(river_perimeter([[1, 0, 1], [1, 1, 1]]))