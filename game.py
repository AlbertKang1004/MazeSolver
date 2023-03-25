"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a MazeGame class."""

import pygame
from sys import exit
from maze import Maze


class MazeGame:
    """MazeGame class where user can run a game.

    Private Instance Attributes:
        - _difficulty: defines the difficulty of the maze (from 1 to 4)
            if the difficulty is in a tuple form (m, n), create a maze of m * n.
        - _time_limit: in seconds, if the time limit is up, the game is over.
        - _cycles: set the number of cycles inside the maze

    Representation Invariants:
        - isinstance(self._difficulty, int) and (1 <= self._difficulty <= 4)
        - isinstance(self._difficulty, tuple[int, int]) and (self._difficulty[0] >= 3 and self._difficulty[1] >= 3)
        - _time_limit >= 10
    """
    _time_limit: int
    maze: Maze
    def __init__(self, difficulty: int | tuple[int, int], time_limit: int, cycles: int = 0) -> None:
        if isinstance(difficulty, int):
            if difficulty == 1:
                maze_size = (7, 7)
            elif difficulty == 1:
                maze_size = (10, 10)
            elif difficulty == 1:
                maze_size = (15, 15)
            elif difficulty == 1:
                maze_size = (20, 20)
            else:
                raise ValueError
        else:  # if self._difficulty is in a tuple form
            maze_size = difficulty

        self._time_limit = time_limit
        self.maze = Maze(maze_size[0], maze_size[1], cycles)


    def run(self) -> None:
        """Run the game!"""
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size())

        black = (0, 0, 0)
        white = (255, 255, 255)
        running = True
        squares = self.draw_maze_on_screen()

        screen.fill(black)
        for square in squares:
            pygame.draw.rect(screen, white, square)
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit()

    def screen_size(self) -> tuple[int, int]:
        return (self.maze.width * 2 + 1) * 25 + 200, (self.maze.height * 2 + 1) * 25 + 200

    def draw_maze_on_screen(self) -> list[pygame.Rect]:
        """return x and y coordinates for the squares"""
        maze_arr = self.maze.maze_graph_to_2d_array()
        squares_so_far = []
        for x in range(len(maze_arr)):
            for y in range(len(maze_arr[0])):
                if maze_arr[x][y] == 0:  # if it is blocked (white)
                    squares_so_far.append(pygame.Rect(x * 25 + 100, y * 25 + 100, 25, 25))
        return squares_so_far

