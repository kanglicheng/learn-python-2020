from collections import deque


def solve(lot):
    visited = set()
    queue = deque()
    # always starts from top left
    queue.append((0, 0))
    distance = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m, n = len(lot), len(lot[0])
    while queue:
        qlength = len(queue)
        for _ in range(qlength):
            cur_c, cur_r = queue.popleft()
            visited.add((cur_r, cur_c))
            if lot[cur_c][cur_r] == 9:
                return distance
            for dc, dr in directions:
                nr, nc = cur_c+dc, cur_r + dr
                if 0 <= nr < m and 0 <= nc < n and lot[nr][nc] != 0 and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        distance += 1
    return -1


lot = [[1, 0, 0],
       [1, 0, 0],
       [1, 9, 1]]
print(solve(lot))
