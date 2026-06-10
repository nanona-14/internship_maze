import pytest
from maze import Maze
from solver import MazeSolver
from  maze_generator import MazeGenerator


# ========================================
# Тесты для Maze
# ========================================

def test_maze_initialization():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    maze = Maze(grid, start=(1,1), end=(1,1))
    
    assert maze.rows == 3
    assert maze.cols == 3
    assert maze.start == (1, 1)
    assert maze.end == (1, 1)


def test_is_valid():
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    maze = Maze(grid, start=(1,1), end=(1,1))
    
    assert maze.is_valid(1, 1) == True
    assert maze.is_valid(0, 0) == False
    assert maze.is_valid(10, 10) == False


def test_get_neighbors():
    grid = [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
    maze = Maze(grid, start=(1,1), end=(1,2))
    neighbors = maze.get_neighbors(1, 1)
    assert (1, 2) in neighbors


# ========================================
# Тесты для MazeGenerator
# ========================================

def test_generator_creates_valid_maze():
    generator = MazeGenerator(rows=15, cols=15)
    grid, start, end = generator.generate()
    
    assert len(grid) == 15
    assert len(grid[0]) == 15
    assert grid[start[0]][start[1]] == 0
    assert grid[end[0]][end[1]] == 0


def test_generated_maze_is_solvable():
    """Критический тест: каждый новый лабиринт должен быть решаемым"""
    generator = MazeGenerator(rows=11, cols=11)
    grid, start, end = generator.generate()
    
    maze = Maze(grid, start=start, end=end)
    solver = MazeSolver(maze)
    path, visited = solver.solve_dfs()
    
    assert path is not None, "Лабиринт должен иметь решение!"


def test_generator_different_each_time():
    generator = MazeGenerator(rows=9, cols=9)
    grid1, _, _ = generator.generate()
    grid2, _, _ = generator.generate()
    
    assert grid1 != grid2


# ========================================
# Тесты для MazeSolver
# ========================================

def test_solver_on_simple_maze():
    grid = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]
    maze = Maze(grid, start=(1,1), end=(3,3))
    solver = MazeSolver(maze)
    path, _ = solver.solve_dfs()
    assert path is not None


# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__, "-v"])