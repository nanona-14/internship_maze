class Maze:
    def __init__(self, grid, start=None, end=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.start = start
        self.end = end
        self.find_start_and_end()

    def find_start_and_end(self):
        if self.start and self.end:
            return
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] in ('S', 2):
                    self.start = (i, j)
                elif self.grid[i][j] in ('E', 3):
                    self.end = (i, j)

    def is_valid(self, x, y):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            return False
        cell = self.grid[x][y]
        return cell in (0, '.', 'S', 'E', 2, 3)

    def get_neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def print_maze(self, path=None):
        """Чистый вывод без лишних пробелов"""
        print("╔" + "═══" * self.cols + "╗")

        for i in range(self.rows):
            line = "║"
            for j in range(self.cols):
                cell = self.grid[i][j]
                
                if path and (i, j) in path:
                    line += " • "      # путь
                elif (i, j) == self.start:
                    line += " S "
                elif (i, j) == self.end:
                    line += " E "
                elif cell == 1 or cell == '#':
                    line += " █ "      # стена
                else:
                    line += "   "      # проход
                    
            line += "║"
            print(line)

            # Горизонтальная линия между рядами
            if i < self.rows - 1:
                print("╠" + "═══" * self.cols + "╣")

        print("╚" + "═══" * self.cols + "╝")
        print()