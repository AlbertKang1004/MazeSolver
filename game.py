"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a MazeGame class."""

import pygame

class MazeGame:
    difficulty: int
    cycles: bool
    time_limit: int
    def __init__(self, difficulty: int, cycles: bool, time_limit: int) -> None:
        self.difficulty = difficulty
        self.cycles = cycles
        self.time_limit = time_limit


