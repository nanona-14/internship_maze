from maze import Maze
from solver import MazeSolver
from maze_generator import MazeGenerator
from tests import *

def main():
    print("=== Генератор лабиринтов + DFS Solver ===\n")
    
    # Создаём генератор
    generator = MazeGenerator(rows=15, cols=15)
    
    # Генерируем новый лабиринт
    grid, start, end = generator.generate()
    
    print(f"Сгенерирован новый лабиринт {len(grid)}×{len(grid[0])}")
    print(f"Старт: {start}, Финиш: {end}\n")
    
    # Создаём объект Maze
    maze = Maze(grid, start=start, end=end)
    
    # Показываем исходный лабиринт
    print("Исходный лабиринт:")
    maze.print_maze()
    
    # Решаем лабиринт
    solver = MazeSolver(maze)
    
    print("\n=== Решение с помощью DFS ===")
    path, visited = solver.solve_dfs()
    
    if path:
        print(f"✅ Путь найден! Длина пути: {len(path)} шагов")
        print("Зелёный • — финальный путь")
        print("Красный • — посещённые клетки и тупики\n")
        maze.print_maze(path=path, visited=visited)
    else:
        print("❌ Путь не найден!")

    print("="*60)


if __name__ == "__main__":
    main()