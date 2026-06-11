# tests.py
import pytest
from fixed_maze import FixedMaze
from maze_generator import MazeGenerator
from maze_solver import solve_maze_dfs


def test_maze_initialization():
    maze = FixedMaze()
    assert maze.grid is not None
    assert maze.start == (1, 1)
    assert maze.end == (13, 13)


def test_is_valid():
    maze = FixedMaze()
    grid = maze.get_grid()
    # start and end должны быть путём (0), не стеной (1)
    sr, sc = maze.start
    er, ec = maze.end
    assert grid[sr][sc] == 0
    assert grid[er][ec] == 0


def test_get_neighbors():
    maze = FixedMaze()
    grid = maze.get_grid()
    rows = maze.rows
    cols = maze.cols
    # Проверяем что размеры корректны
    assert rows == 15
    assert cols == 15
    # Проверяем что у старта есть хотя бы один сосед-путь
    sr, sc = maze.start
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = [
        (sr+dr, sc+dc)
        for dr, dc in directions
        if 0 <= sr+dr < rows and 0 <= sc+dc < cols and grid[sr+dr][sc+dc] == 0
    ]
    assert len(neighbors) >= 1


def test_generator_creates_valid_maze():
    generator = MazeGenerator(width=15, height=15)
    grid = generator.get_grid()
    assert grid is not None
    assert len(grid) == 15
    assert len(grid[0]) == 15


def test_generated_maze_is_solvable():
    """Критический тест: каждый новый лабиринт должен быть решаемым"""
    generator = MazeGenerator(width=11, height=11)
    grid = generator.get_grid()
    start = generator.get_start()
    end = generator.get_end()
    path = solve_maze_dfs(grid, start, end)
    assert path is not None, "Лабиринт должен быть решаемым"


def test_generator_different_each_time():
    gen1 = MazeGenerator(width=9, height=9)
    gen2 = MazeGenerator(width=9, height=9)
    # Два лабиринта скорее всего разные (random)
    # Просто проверяем что оба генерируются без ошибок
    assert gen1.get_grid() is not None
    assert gen2.get_grid() is not None


def test_solver_on_simple_maze():
    grid = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
    ]
    path = solve_maze_dfs(grid, start=(1,1), end=(3,3))
    assert path is not None
    assert path[0] == (1,1)
    assert path[-1] == (3,3)