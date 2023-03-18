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
        - _cycles: set if there is a cycle in the maze,
            which causes the maze to have multiple solutions
        - _time_limit: in seconds, if the time limit is up, the game is over.

    Representation Invariants:
        - isinstance(self._difficulty, int) and (1 <= self._difficulty <= 4)
        - isinstance(self._difficulty, tuple[int, int]) and (self._difficulty[0] >= 3 and self._difficulty[1] >= 3)
        - _time_limit >= 10
    """
    _difficulty: int | tuple[int, int]
    _cycles: bool
    _time_limit: int
    maze: Maze
    def __init__(self, difficulty: int, cycles: bool, time_limit: int) -> None:
        self._difficulty = difficulty
        self._cycles = cycles
        self._time_limit = time_limit


    def run(self) -> None:
        """Run the game!"""
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size())

        black = (0, 0, 0)
        white = (255, 255, 255)
        running = True
        while running:
            screen.fill(black)
            squares = self.draw_maze_on_screen()
            for square in squares:
                pygame.draw.rect(screen, white, pygame.Rect(square[0], square[1], square[0] + 25, square[1] + 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit()
    def maze_size(self) -> tuple[int, int]:
        """Decide how big the size of the screen have to be, in order to contain the maze.
        each blocks of the maze will be 25 * 25 in size,
        and the whole maze will be hovered with a space of 100 pixels.
        """
        if isinstance(self._difficulty, int):
            if self._difficulty == 1:
                maze_size = (7, 7)
            elif self._difficulty == 1:
                maze_size = (10, 10)
            elif self._difficulty == 1:
                maze_size = (15, 15)
            elif self._difficulty == 1:
                maze_size = (20, 20)
            else:
                raise ValueError
        else:  # if self._difficulty is in a tuple form
            maze_size = self._difficulty
        # screen_size = (maze_size[0] * 2 + 1) * 30 + 200, (maze_size[1] * 2 + 1) * 30 + 200
        return maze_size

    def screen_size(self) ->  :

    def draw_maze_on_screen(self) -> list[tuple]:
        """return x and y coordinates for the squares"""
        maze_arr = self.maze.maze_graph_to_2d_array()
        squares_so_far = []
        for x in range(len(maze_arr)):
            for y in range(len(maze_arr[0])):
                if maze_arr[x][y] == 0:  # if it is blocked (white)
                    squares_so_far.append((x * 25 + 100, y * 25 + 100))
        return squares_so_far

