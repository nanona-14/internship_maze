# # maze_solver.py
# from collections import deque


# def solve_maze_bfs(grid, start, end):
#     """
#     Solve maze using BFS and return the shortest path as list of (row, col) tuples.
#     Returns None if no path exists.
#     """
#     if not grid or not start or not end:
#         return None

#     rows, cols = len(grid), len(grid[0])
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

#     queue = deque([(start, [start])])
#     visited = set([start])

#     while queue:
#         (r, c), path = queue.popleft()

#         if (r, c) == end:
#             return path

#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc

#             if (0 <= nr < rows and 0 <= nc < cols and
#                 grid[nr][nc] == 0 and (nr, nc) not in visited):
#                 visited.add((nr, nc))
#                 queue.append(((nr, nc), path + [(nr, nc)]))
#     return None  # No path found









# maze_solver.py
from collections import deque
def solve_maze_dfs(grid, start, end):
    """
    Solve maze using DFS and return a path as list of (row, col) tuples.
    Returns None if no path exists.
    """
    if not grid or not start or not end:
        return None

    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    stack = [(start, [start])]          # ← deque заменили на обычный list (stack)
    visited = set([start])

    while stack:
        (r, c), path = stack.pop()      # ← popleft() заменили на pop()

        if (r, c) == end:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and (nr, nc) not in visited):

                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None  # No path found