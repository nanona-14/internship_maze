# maze_generator.py
import random
from collections import deque


class MazeGenerator:
    def __init__(self, width=15, height=15):
        self.width = width
        self.height = height
        self.start = (1, 1)
        self.end = (height - 2, width - 2)
        self.grid = None
        self.generate()

    def generate(self):
        """Generate a random perfect maze using Recursive Backtracking"""
        # Initialize grid with walls
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]

        def carve(x, y):
            self.grid[y][x] = 0
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width and 0 <= ny < self.height and
                        self.grid[ny][nx] == 1):
                    self.grid[y + dy // 2][x + dx // 2] = 0
                    carve(nx, ny)

        # Start carving from start position
        carve(self.start[1], self.start[0])  # (x, y) -> (col, row)

        # Ensure start and end are open
        self.grid[self.start[0]][self.start[1]] = 0
        self.grid[self.end[0]][self.end[1]] = 0

    def get_grid(self):
        return self.grid

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def print_maze(self, path=None):
        """Print maze to terminal"""
        grid = [row[:] for row in self.grid]

        if path:
            for r, c in path:
                if grid[r][c] == 0:
                    grid[r][c] = 2

        symbols = {1: "██", 0: "  ", 2: "••"}

        print(f"\nRandom Maze ({self.width}x{self.height}):")
        for row in grid:
            print("".join(symbols.get(cell, "  ") for cell in row))

        print(f"Start (S): {self.start} | End (E): {self.end}")