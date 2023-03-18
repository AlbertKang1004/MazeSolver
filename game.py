"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a MazeGame class."""

import pygame
from sys import exit


class MazeGame:
    """MazeGame class where user can run a game.

    Private Instance Attributes"""
    _difficulty: int
    _cycles: bool
    _time_limit: int
    def __init__(self, difficulty: int, cycles: bool, time_limit: int) -> None:
        self._difficulty = difficulty
        self._cycles = cycles
        self._time_limit = time_limit

    #test

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
