# demo.py
from fixed_maze import FixedMaze
from maze_solver import solve_maze_bfs
from maze_generator import MazeGenerator


def main():
    print("=== Maze Solver Demo ===\n")

    # 1. Fixed Maze
    print("1. Fixed Maze")
    fixed = FixedMaze()
    fixed.print_maze()

    path1 = solve_maze_bfs(fixed.get_grid(), fixed.get_start(), fixed.get_end())
    if path1:
        print(f"Path found! Length: {len(path1)} steps")
        fixed.print_maze(path1)
    else:
        print("No path found!")

    # 2. Random Maze
    print("\n" + "="*50)
    print("2. Random Maze")
    random_maze = MazeGenerator(width=17, height=13)
    random_maze.print_maze()

    path2 = solve_maze_bfs(random_maze.get_grid(), random_maze.get_start(), random_maze.get_end())
    if path2:
        print(f"Path found! Length: {len(path2)} steps")
        random_maze.print_maze(path2)
    else:
        print("No path found!")


if __name__ == "__main__":
    main()