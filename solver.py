from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve_dfs(self):
        """DFS с возвратом (backtracking) — возвращает путь и все посещённые клетки"""
        if not self.maze.start or not self.maze.end:
            return None, set()

        visited = set()
        stack = [(self.maze.start, [self.maze.start])]
        dead_ends = set()   # клетки, из которых пришлось вернуться

        while stack:
            (x, y), current_path = stack.pop()
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))

            if (x, y) == self.maze.end:
                return current_path, visited  # нашли путь

            # Проверяем соседей
            added = False
            for nx, ny in self.maze.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    stack.append(((nx, ny), current_path + [(nx, ny)]))
                    added = True

            # Если нет соседей — это тупик
            if not added and (x, y) != self.maze.start:
                dead_ends.add((x, y))

        return None, visited  # пути нет