from collections import deque


def dfs(grid: list[list[int]], i: int, j: int, visited: set[list[int]]):
    # check boundary conditions
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited:
        return

    print(grid[i][j], end=" ")
    visited.add((i, j))
    dfs(grid, i + 1, j, visited)  # right
    dfs(grid, i - 1, j, visited)  # left
    dfs(grid, i, j + 1, visited)  # up
    dfs(grid, i, j - 1, visited)  # down


def bfs(grid: list[list[int]], startRow: int, startCol: int):
    q = deque([(startRow, startCol)])
    visited = set([(startRow, startCol)])

    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))  # left, right, up, down
    while q:
        curr = q.popleft()
        print(grid[curr[0]][curr[1]], end=" ")

        for dir in dirs:
            i = curr[0] + dir[0]
            j = curr[1] + dir[1]
            # check boundary conditions
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited:
                continue
            visited.add((i, j))
            q.append((i, j))


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("DFS: ", end="")
dfs(grid, 0, 0, set())
print()
print("BFS: ", end="")
bfs(grid, 0, 0)
