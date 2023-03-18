"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a MazeGame class."""

import pygame
from sys import exit


#hellneeo 3
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
    def __init__(self, difficulty: int, cycles: bool, time_limit: int) -> None:
        self._difficulty = difficulty
        self._cycles = cycles
        self._time_limit = time_limit


    def run(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode((200, 200))

        red = (255, 0, 0)
        running = True
        while running:
            screen.fill(red)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        exit()
    # def create_screen_size(self) -> tuple[int, int]:
    # if self._difficulty == '1': # Easy
