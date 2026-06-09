from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve_dfs(self):
        """DFS алгоритм для поиска пути"""
        if not self.maze.start or not self.maze.end:
            return None

        visited = set()
        stack = [(self.maze.start, [self.maze.start])]

        while stack:
            (x, y), current_path = stack.pop()
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))

            if (x, y) == self.maze.end:
                return current_path

            for nx, ny in self.maze.get_neighbors(x, y):
                if (nx, ny) not in visited:
                    stack.append(((nx, ny), current_path + [(nx, ny)]))

        return None  # пути нет

    # def solve_bfs(self):
    #     """BFS алгоритм (для сравнения, находит самый короткий путь)"""
    #     if not self.maze.start or not self.maze.end:
    #         return None

    #     visited = set()
    #     queue = deque([(self.maze.start, [self.maze.start])])

    #     while queue:
    #         (x, y), current_path = queue.popleft()
            
    #         if (x, y) in visited:
    #             continue
                
    #         visited.add((x, y))

    #         if (x, y) == self.maze.end:
    #             return current_path

    #         for nx, ny in self.maze.get_neighbors(x, y):
    #             if (nx, ny) not in visited:
    #                 queue.append(((nx, ny), current_path + [(nx, ny)]))

        return None