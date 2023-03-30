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
    """Run a code that prints the randomized maze using the square emote.

        - width: The width of the maze
        - height: The height of the maze
        - cycles: The number of cycles (or added edges), default = 0
    """
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
    """Run a pygame console with a randomized maze.
    Press arrow keys to move the player.

        - difficulty: Represents the difficulty of the maze. Allows type int or tuple[int, int].
            - 1: Easy
            - 2: Intermediate
            - 3: Hard
            - 4: Expert
            - (x, y): Custom
        - time_limit: The time allowed for the player (in seconds)
        - cycles: The number of cycles (or added edges), default = 0
        """
    g = MazeGame(difficulty, time_limit, cycles)
    g.run()


