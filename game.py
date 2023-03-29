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
from typing import Any
import python_ta

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
    pixel: int = 20
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
        clock = pygame.time.Clock()
        counter, timer_text = self._time_limit, str(self._time_limit).rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        timer_font = pygame.font.Font('font/timer.ttf', 50)

        running = True
        w, h = screen.get_width(), screen.get_height()
        mw, mh = self.maze.width, self.maze.height
        squares = self.draw_maze_on_screen()
        squares.append(pygame.Rect(self.pixel, 0, self.pixel, 1))
        # This is the square that blocks the entrance so that player cannot go out of the maze.

        # Starting Points
        x, y = 100 + self.pixel + 2, 102

        background = pygame.Surface(self.screen_size())
        for square in squares:
            if square.x == self.pixel and square.y == 0:
                pygame.draw.rect(background, pygame.Color('black'), square)
                # Since we don't want to see starting point blocked by a white square, we will make it invisible.
            else:
                pygame.draw.rect(background, pygame.Color('white'), square)

        screen.fill(pygame.Color('black'))
        while running:
            player = pygame.Rect(x, y, self.pixel - 5, self.pixel - 5)
            endpoint = pygame.Rect(w - 2 * self.pixel - 100, h - self.pixel - 100,
                                   self.pixel, self.pixel)
            t, l, r, b = player.midtop, player.midleft, player.midright, player.midbottom
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    if counter >= 0:
                        timer_text = str(counter).rjust(3)
                    else:
                        draw_solution_path(self.maze, background, 'red', self.pixel)
                        screen.blit(background, (100, 100))
                        print_on_screen(screen, 'font/answer.ttf', 50, "ANSWER", 'red', (w / 2, 50))
                        pygame.time.delay(5000)

                        screen.fill(pygame.Color('black'))
                        print_on_screen(screen, 'font/game_over.ttf', 50, "GAME OVER", 'red', (w / 2, h / 2))
                        pygame.time.delay(3000)
                        exit()
                if event.type == pygame.QUIT:
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                if not any(square.collidepoint(l[0] - 100, l[1] - 100) for square in squares):
                    x -= 2
            if key[pygame.K_RIGHT]:
                if not any(square.collidepoint(r[0] - 100, r[1] - 100) for square in squares):
                    x += 2
            if key[pygame.K_UP]:
                if not any(square.collidepoint(t[0] - 100, t[1] - 100) for square in squares):
                    y -= 2
            if key[pygame.K_DOWN]:
                if not any(square.collidepoint(b[0] - 100, b[1] - 100) for square in squares):
                    y += 2
            if endpoint.collidepoint(b):
                screen.fill(pygame.Color('black'))
                print_on_screen(screen, 'font/game_over.ttf', 50, "YOU WIN", 'brown', (w / 2, h / 2))
                pygame.time.delay(3000)
                exit()

            screen.fill(pygame.Color('black'))
            screen.blit(background, (100, 100))

            pygame.draw.rect(screen, pygame.Color('red'), player)
            pygame.draw.rect(screen, pygame.Color('goldenrod'), endpoint)

            pygame.time.delay(10)
            screen.blit(timer_font.render(timer_text, True, pygame.Color('white')), (w - 100, 30))
            pygame.display.flip()
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
                    squares_so_far.append(pygame.Rect(x * self.pixel, y * self.pixel,
                                                      self.pixel, self.pixel))
        return squares_so_far

def print_on_screen(screen: pygame.Surface, font: str, font_size: int, text: str, color: str, text_loc: Any) -> None:
    """Print text on the game screen."""
    f = pygame.font.Font(font, font_size)
    t = f.render(text, True, pygame.Color(color))
    tr = t.get_rect(center=text_loc)
    screen.blit(t, tr)
    pygame.display.update()
def draw_solution_path(maze: Maze, screen: pygame.Surface, color: str, pixel: int) -> None:
    """Draw the line that shows the solution."""
    mw, mh = maze.width, maze.height
    path = maze.find_solution()
    pygame.draw.line(screen, pygame.Color(color), (1.5 * pixel, 0),
                     (1.5 * pixel, 1.5 * pixel), width=5)
    pygame.draw.line(screen, pygame.Color(color),
                     ((2 * mw - 0.5) * pixel,
                      (2 * mh - 0.5) * pixel),
                     ((2 * mw - 0.5) * pixel, (2 * mh + 1) * pixel),
                     width=5)
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        pygame.draw.line(screen, pygame.Color(color),
                         ((2 * x1 + 1.5) * pixel, (2 * y1 + 1.5) * pixel),
                         ((2 * x2 + 1.5) * pixel, (2 * y2 + 1.5) * pixel),
                         width=5)

# python_ta.check_all(config={
#     'extra-imports': [],  # the names (strs) of imported modules
#     'allowed-io': [],     # the names (strs) of functions that call print/open/input
#     'max-line-length': 120
# })
