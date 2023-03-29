"""CSC111 Group Project: Maze Solver

$$\      $$\
$$$\    $$$ |
$$$$\  $$$$ | $$$$$$\  $$$$$$$$\  $$$$$$\
$$\$$\$$ $$ | \____$$\ \____$$  |$$  __$$\
$$ \$$$  $$ | $$$$$$$ |  $$$$ _/ $$$$$$$$ |
$$ |\$  /$$ |$$  __$$ | $$  _/   $$   ____|
$$ | \_/ $$ |\$$$$$$$ |$$$$$$$$\ \$$$$$$$\
\__|     \__| \_______|\________| \_______|
 $$$$$$\            $$\
$$  __$$\           $$ |
$$ /  \__| $$$$$$\  $$ |$$\    $$\  $$$$$$\   $$$$$$\
\$$$$$$\  $$  __$$\ $$ |\$$\  $$  |$$  __$$\ $$  __$$\
 \____$$\ $$ /  $$ |$$ | \$$\$$  / $$$$$$$$ |$$ |  \__|
$$\   $$ |$$ |  $$ |$$ |  \$$$  /  $$   ____|$$ |
\$$$$$$  |\$$$$$$  |$$ |   \$  /   \$$$$$$$\ $$ |
 \______/  \______/ \__|    \_/     \_______|\__|

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file is used to run the MazeSolver.

The additional description on how to use the program is listed below."""

from maze import Maze
from game import MazeGame

def runner_maze(width: int, height: int, cycles: int = 0, show_solution: bool = False) -> None:
    """runner example for the maze"""
    m = Maze(width, height, cycles)
    maze = m.maze_graph_to_2d_array(show_solution)
    for y in range(len(maze[0])):
        for x in range(len(maze)):
            if maze[x][y] == 2:
                print('🟫', end="")
            elif maze[x][y] == 1:
                print('⬛', end="")
            else:
                print('⬜', end="")
        print()

def runner_pygame(difficulty: int | tuple[int, int], time_limit: int, cycles: int = 0) -> None:
    """runner example for the pygame maze console"""
    g = MazeGame(difficulty, time_limit, cycles)
    g.run()


