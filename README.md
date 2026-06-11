# 🌀 Internship Maze

A Python project that generates and solves mazes using DFS.

## 📁 Project Structure

```
internship_maze/
├── fixed_maze.py       # Fixed 15x15 hardcoded maze
├── maze_generator.py   # Random maze generator (Recursive Backtracking)
├── maze_solver.py      # DFS maze solver
├── demo.py             # Demo: runs both fixed and random maze
├── tests.py            # Pytest tests
└── README.md
```

## ⚙️ How It Works

- **`FixedMaze`** — a hardcoded 15x15 maze. Start: `(1,1)`, End: `(13,13)`. Grid uses `0` for paths and `1` for walls.
- **`MazeGenerator`** — generates a random perfect maze of any size using the Recursive Backtracking algorithm.
- **`solve_maze_dfs`** — solves any maze using DFS and returns the shortest path as a list of `(row, col)` tuples.

## 🚀 Getting Started

### Requirements

- Python 3.11+
- pytest (for tests)

### Install dependencies

```bash
pip install pytest
```

### Run the demo

```bash
python demo.py
```

### Run tests

```bash
python -m pytest tests.py -v
```

## 📌 Usage Example

```python
from fixed_maze import FixedMaze
from maze_solver import solve_maze_bfs

maze = FixedMaze()
path = solve_maze_dfs(maze.get_grid(), maze.get_start(), maze.get_end())
print(f"Path length: {len(path)} steps")
maze.print_maze(path)
```

```python
from maze_generator import MazeGenerator
from maze_solver import solve_maze_dfs

gen = MazeGenerator(width=21, height=21)
path = solve_maze_dfs(gen.get_grid(), gen.get_start(), gen.get_end())
print(f"Path length: {len(path)} steps")
gen.print_maze(path)
```

## ✅ Tests

| Test | Description |
|------|-------------|
| `test_maze_initialization` | FixedMaze loads correctly |
| `test_is_valid` | Start and end are walkable cells |
| `test_get_neighbors` | Maze is 15x15 and has valid neighbors |
| `test_generator_creates_valid_maze` | Generator produces correct size grid |
| `test_generated_maze_is_solvable` | Every generated maze has a solution |
| `test_generator_different_each_time` | Generator runs without errors |
| `test_solver_on_simple_maze` | DFS finds correct path |
