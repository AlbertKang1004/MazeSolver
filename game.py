"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaan Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a MazeGame class."""

from typing import Any
import pygame
from maze import Maze


class MazeGame:
    """MazeGame class where user can run a game.

    Instance Attributes:
        - maze: the maze given to the pygame console.
        - pixel: specifies the size of the each pixel, default at 20.

    Private Instance Attributes:
        - _time_limit: in seconds, if the time limit is up, the game is over.

    Representation Invariants:
        - isinstance(self._difficulty, tuple[int, int]) and (self._difficulty[0] >= 3 and self._difficulty[1] >= 3)
        - self._time_limit >= 1
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
                maze_size = (10, 10)  # Default Case
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

        # Starting Point for the Player
        x, y = 100 + self.pixel + 2, 102

        squares = self.create_squares()
        background = self.draw_maze_on_surface(squares)

        screen.fill(pygame.Color('black'))
        while running:
            player = pygame.Rect(x, y, self.pixel - 5, self.pixel - 5)
            endpoint = pygame.Rect(w - 2 * self.pixel - 100, h - self.pixel - 100,
                                   self.pixel, self.pixel)
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

            x, y = check_collison_and_move(player, squares)

            if endpoint.collidepoint(player.midbottom):
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

    def create_squares(self) -> list[pygame.Rect]:
        """return x and y coordinates for the squares"""
        maze_arr = self.maze.maze_graph_to_2d_array()
        squares_so_far = []
        for x in range(len(maze_arr)):
            for y in range(len(maze_arr[0])):
                if maze_arr[x][y] == 0:  # if it is blocked (white)
                    squares_so_far.append(pygame.Rect(x * self.pixel, y * self.pixel,
                                                      self.pixel, self.pixel))
        return squares_so_far

    def draw_maze_on_surface(self, squares: list[pygame.Rect]) -> pygame.Surface:
        """Draw a maze on the given surface using the squares given."""
        background = pygame.Surface(self.screen_size())
        squares.append(pygame.Rect(self.pixel, 0, self.pixel, 1))
        for square in squares:
            if square.x == self.pixel and square.y == 0:
                pygame.draw.rect(background, pygame.Color('black'), square)
                # Since we don't want to see starting point blocked by a white square, we will make it invisible.
            else:
                pygame.draw.rect(background, pygame.Color('white'), square)
        return background


def check_collison_and_move(player: pygame.Rect, maze: list[pygame.Rect]) -> tuple[int, int]:
    """Check if the player is collided to the wall and decide to move or not."""
    t, l, r, b = player.midtop, player.midleft, player.midright, player.midbottom
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if not any(square.collidepoint(l[0] - 100, l[1] - 100) for square in maze):
            return player.x - 2, player.y
    if key[pygame.K_RIGHT]:
        if not any(square.collidepoint(r[0] - 100, r[1] - 100) for square in maze):
            return player.x + 2, player.y
    if key[pygame.K_UP]:
        if not any(square.collidepoint(t[0] - 100, t[1] - 100) for square in maze):
            return player.x, player.y - 2
    if key[pygame.K_DOWN]:
        if not any(square.collidepoint(b[0] - 100, b[1] - 100) for square in maze):
            return player.x, player.y + 2
    return player.x, player.y


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


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['pygame', 'maze', 'sys', 'typing'],
        'allowed-io': [],
        'disable': ['E9992', 'E9997', 'E9998', 'E1101']
    })
