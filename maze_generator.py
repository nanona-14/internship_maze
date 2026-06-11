import random

class MazeGenerator:
    def __init__(self, rows=21, cols=21):
        self.rows = rows
        self.cols = cols

    def generate(self):
        """Generation (Recursive Backtracking)"""
        grid = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Начинаем с нечётной клетки
        cx = random.randrange(1, self.rows - 1, 2)
        cy = random.randrange(1, self.cols - 1, 2)
        
        self._carve_passages(grid, cx, cy)
        
        # Вход и выход
        start = (0, 1)
        end = (self.rows-1, self.cols-2)
        grid[0][1] = 0
        grid[self.rows-1][self.cols-2] = 0
        
        return grid, start, end

    def _carve_passages(self, grid, cx, cy):
        grid[cx][cy] = 0
        
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if (0 < nx < self.rows-1 and 0 < ny < self.cols-1 and grid[nx][ny] == 1):
                grid[cx + dx//2][cy + dy//2] = 0
                self._carve_passages(grid, nx, ny)


