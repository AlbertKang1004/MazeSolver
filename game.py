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
    pixel = 20
    def __init__(self, difficulty: int | tuple[int, int], time_limit: int, cycles: int = 0) -> None:
        if isinstance(difficulty, int):
            if difficulty == 1:
                maze_size = (7, 7)
            elif difficulty == 2:
                maze_size = (10, 10)
            elif difficulty == 3:
                maze_size = (15, 15)
            elif difficulty == 4:
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

        running = True
        squares = self.draw_maze_on_screen()
        squares.append(pygame.Rect(100 + self.pixel, 100 - self.pixel, self.pixel, self.pixel))
        # This is the square that blocks the entrance so that player cannot go out of the maze.

        # Starting Points
        x, y = 100 + self.pixel + 2, 100

        background = pygame.Surface(self.screen_size())
        for square in squares:
            if square.x == 100 + self.pixel and square.y == 100 - self.pixel:
                pygame.draw.rect(background, pygame.Color('black'), square)
                # Since we don't want to see starting point blocked by a white square, we will make it invisible.
            else:
                pygame.draw.rect(background, pygame.Color('white'), square)

        screen.fill(pygame.Color('black'))
        while running:
            player = pygame.Rect(x, y, self.pixel - 5, self.pixel - 5)
            endpoint = pygame.Rect(screen.get_width() - 2 * self.pixel - 100, screen.get_height() - self.pixel - 100,
                                   self.pixel, self.pixel)
            t, l, r, b = player.midtop, player.midleft, player.midright, player.midbottom
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                if not any(square.collidepoint(l) for square in squares):
                    x -= 2
            if key[pygame.K_RIGHT]:
                if not any(square.collidepoint(r) for square in squares):
                    x += 2
            if key[pygame.K_UP]:
                if not any(square.collidepoint(t) for square in squares):
                    y -= 2
            if key[pygame.K_DOWN]:
                if not any(square.collidepoint(b) for square in squares):
                    y += 2
            if endpoint.collidepoint(b):
                font = pygame.font.Font('Fira Code', 100)
                text = font.render("You win!", True, pygame.Color('green'))
                text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.delay(5000)
                exit()

            screen.fill(pygame.Color('black'))
            screen.blit(background, (0, 0))

            pygame.draw.rect(screen, pygame.Color('red'), player)
            pygame.draw.rect(screen, pygame.Color('goldenrod'), endpoint)
            pygame.time.delay(10)
            pygame.display.update()
        exit()

    def screen_size(self) -> tuple[int, int]:
        """Calculates how big the screen should be"""
        return (self.maze.width * 2 + 1) * self.pixel + 200, (self.maze.height * 2 + 1) * self.pixel + 200

    def draw_maze_on_screen(self) -> list[pygame.Rect]:
        """return x and y coordinates for the squares"""
        maze_arr = self.maze.maze_graph_to_2d_array()
        squares_so_far = []
        for x in range(len(maze_arr)):
            for y in range(len(maze_arr[0])):
                if maze_arr[x][y] == 0:  # if it is blocked (white)
                    squares_so_far.append(pygame.Rect(x * self.pixel + 100, y * self.pixel + 100,
                                                      self.pixel, self.pixel))
        return squares_so_far

