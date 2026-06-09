class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = None
        self.end = None
        self.find_start_and_end()

    def find_start_and_end(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'S':
                    self.start = (i, j)
                elif self.grid[i][j] == 'E':
                    self.end = (i, j)

    def is_valid(self, x, y):
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] != '#')

    def get_neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def print_maze(self, path=None):
        """Красивый вывод лабиринта с реальными линиями стен"""
        wall = '█'      # толстая стена
        path_char = '•' # точка для пути
        empty = ' '     # пустое пространство

        print("╔" + "═══" * self.cols + "╗")
        
        for i in range(self.rows):
            line = "║"
            for j in range(self.cols):
                cell = self.grid[i][j]
                
                if path and (i, j) in path:
                    line += f" {path_char} "   # путь
                elif cell == 'S':
                    line += " S "
                elif cell == 'E':
                    line += " E "
                elif cell == '#':
                    line += f" {wall} "
                else:
                    line += f" {empty} "
            line += "║"
            print(line)
            
            # Горизонтальные линии между рядами
            if i < self.rows - 1:
                print("╠" + "═══" * self.cols + "╣")
        
        print("╚" + "═══" * self.cols + "╝")
        print()