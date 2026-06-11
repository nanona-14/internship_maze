from maze import Maze
from solver import MazeSolver
from maze_generator import MazeGenerator
from tests import *

def main():
    print("=== Maze Generator + DFS Solver ===\n")
    
    # Создаём генератор
    generator = MazeGenerator(rows=15, cols=15)
    
    # Генерируем новый лабиринт
    grid, start, end = generator.generate()
    
    print(f"Generated new maze {len(grid)}×{len(grid[0])}")
    print(f"Start: {start}, End: {end}\n")
    
    # Создаём объект Maze
    maze = Maze(grid, start=start, end=end)
    
    # Показываем исходный лабиринт
    print("Current maze:")
    maze.print_maze()
    
    # Решаем лабиринт
    solver = MazeSolver(maze)
    
    print("\n=== The solution with DFS ===")
    path, visited = solver.solve_dfs()
    
    if path:
        print(f"✅ The path is found! The length of the path: {len(path)} steps")
        print("Green • — final path")
        print("Red • — visited parts\n")
        maze.print_maze(path=path, visited=visited)
    else:
        print("❌ The path is not found!")

    print("="*60)


if __name__ == "__main__":
    main()