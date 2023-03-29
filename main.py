"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file is used to run the MazeSolver.

The additional description on how to use the program is listed below."""

import python_ta
import

def runner_maze() -> None:


def runner_pygame() -> None:


print(r"""
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
 """)

print("Select One of the option: \n"
      "1. Display the maze\n"
      "2. Solve the maze\n")
c = int(input("Your Choice: "))
if c == 1:
    width = int(input("Please set the width of the maze (>= 3): "))
    height = int(input("Please set the height of the maze (>= 3): "))
    display_solution = True if input("Do you want to see the solutions together? Type Y if you want to: ") == 'Y' else False

elif c == 2:
    difficulty = int(input("Please choose the difficulty of a maze: "
                           "1. Easy (7 * 7)"
                           "2. Intermediate (10 * 10"
                           "3. Hard (15 * 15)"
                           "4. Extreme (20 * 20)"
                           "5. Custom (You can choose the size)"))

    width = int(input("Please set the width of the maze (>= 3): "))
    height = int(input("Please set the height of the maze (>= 3): "))
else:
    raise ValueError

