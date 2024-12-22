def solve(matrix):
    def dfs(r, c, visited):
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                if matrix[nr][nc] == matrix[r][c] + 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)

    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                visited = {(r, c)}
                dfs(r, c, visited)
                if any(matrix[x][y] == 9 for x, y in visited):
                    count += sum(1 for x, y in visited if matrix[x][y] == 9)
    print(count)


def solve2(matrix):
    """
    Count the number of distinct paths from 0 to 9 in the matrix, for
    each 0 cell in the matrix.
    """

    def dfs(r, c, visited):
        if matrix[r][c] == 9:
            return 1
        paths = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                if matrix[nr][nc] == matrix[r][c] + 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    paths += dfs(nr, nc, visited)
                    visited.remove((nr, nc))
        return paths

    total_paths = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                visited = {(r, c)}
                total_paths += dfs(r, c, visited)
    print(total_paths)


with open("input10.txt") as file:
    m = []
    for line in file:
        row = []
        for n in line:
            if n == "\n":
                continue
            row.append(int(n))
        m.append(row)
    solve(m)
    solve2(m)
