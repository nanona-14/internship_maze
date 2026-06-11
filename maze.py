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

    
    def print_maze(self, path=None, visited=None, dead_ends=None):
        """Красивый вывод лабиринта как на картинке — чистые толстые стены"""
        RESET = '\033[0m'
        GREEN = '\033[92m'
        RED = '\033[91m'
        YELLOW = '\033[93m'

        WALL = '║║'           # толстая стена
        OPEN = '  '           # открытый проход
        SOL_PATH = f"{GREEN}••{RESET}"   # зелёный путь
        VISITED_MARK = f"{RED}••{RESET}" # красные посещённые/тупики

        # Верхняя граница
        print("╔" + "══" * self.cols + "╗")

        for i in range(self.rows):
            line = "║"
            for j in range(self.cols):
                pos = (i, j)

                if path and pos in path:
                    line += SOL_PATH
                elif (dead_ends and pos in dead_ends) or (visited and pos in visited):
                    line += VISITED_MARK
                elif pos == self.start:
                    line += f"{YELLOW}S{RESET}"
                elif pos == self.end:
                    line += f"{YELLOW}E{RESET}"
                elif self.grid[i][j] == 1 or self.grid[i][j] == '#':
                    line += WALL
                else:
                    line += OPEN

            line += "║"
            print(line)

            # Горизонтальная линия
            

        # Нижняя граница
        print("╚" + "══" * self.cols + "╝")
        print()