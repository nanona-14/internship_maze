# Maze Project — Generator & Solver

A Python project that **generates random mazes** and **solves** them using the **DFS** (Depth-First Search) algorithm.  
Developed using **TDD** (Test-Driven Development).

## Features

- Random Maze Generator (15×15) using **Recursive Backtracking**
- DFS Solver that finds the path from Start (`S`) to End (`E`)
- Beautiful terminal visualization with colors:
  - **Green** `•` — Final solution path
  - **Red** `•` — Visited cells and dead-ends (backtracking)
- Unit tests with pytest
- Clean, modular code structure


## Project Structure
maze/                   
└── internship_maze/
|   ├── main.py                # Main entry point 
|   ├── tests.py               # Unit tests (pytest)
│   ├── maze.py                # Maze class + colored printing
│   ├── solver.py              # DFS Solver
│   └── maze_generator.py      # Random maze generator       


## How to Run

```powershell
# 1. Go to project folder
cd internship_maze

# 2. Run the main program (creates a new maze every time)
python main.py

# 3. Run all tests
python -m pytest -v