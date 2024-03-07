"""
            1 - 0 - 6
           / \
          2   3
           \ / \
            4 - 5  
"""
from collections import deque


graph = {
    0: [1, 6],
    1: [0, 2, 3],
    2: [1, 4],
    3: [1, 4, 5],
    4: [2, 3, 5],
    5: [3, 4],
    6: [0]
}


# DFS uses recursion and maintains a visited set, recursing thru each node's neighbors
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS uses a queue and maintains a visited set
# It uses a while loops and visits each neighbor, adding it to the q and visited set


def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)


print("DFS:")
dfs(graph, 2)
print("\nBFS:")
bfs(graph, 3)
