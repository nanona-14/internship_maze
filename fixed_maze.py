# fixed_maze.py
class FixedMaze:
    def __init__(self):
        # Fixed 15x15 maze
        # 0 = path, 1 = wall
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,0,1,0,1,0,1,0,1],
            [1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
            [1,1,1,0,1,0,1,1,1,0,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.start = (1, 1)   # (row, col)
        self.end = (13, 13)

    def get_grid(self):
        return self.grid

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def print_maze(self, path=None):
        """Print maze in terminal"""
        grid = [row[:] for row in self.grid]  # copy
        
        if path:
            for r, c in path:
                if grid[r][c] == 0:
                    grid[r][c] = 2  # mark path
        
        symbols = {1: "██", 0: "  ", 2: "••"}
        
        print("\nFixed Maze:")
        for row in grid:
            print("".join(symbols[cell] for cell in row))
        
        print(f"Start (S): {self.start} | End (E): {self.end}")