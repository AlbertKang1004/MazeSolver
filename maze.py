"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaas Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a maze class, which includes various fundcions."""

from graph import Graph
from copy import deepcopy
import random
# from python_ta.contracts import check_contracts


# @check_contracts
class Maze:
    """A Maze represented in a graph.

    Instance Attributes:
        - height: the height of the maze
        - width: the width of the maze
        - MazeGraph: the graph representation of maze
        - edges: the edges that this graph have
        - cycles: number of cycles in the maze

    Representation Invariants:
        - height >= 3 and width >= 3
        - start_point[0] == 0
        - end_point[0] == height - 1
    """
    height: int
    width: int
    MazeGraph: Graph
    edges: list[tuple]
    cycles: int
    _removed_edges: list[tuple]

    def __init__(self, width: int, height: int, cycles: int = 0) -> None:
        """Initialize a maze with a specified width and height"""
        self.height = height
        self.width = width
        self.cycles = cycles
        self.MazeGraph = Graph()
        # First, initialize all the vertices, in a x * y size.
        full_graph = Graph()
        for x in range(width):
            for y in range(height):
                full_graph.add_vertex(x, y)
                self.MazeGraph.add_vertex(x, y)

        # Then, connect all the vertices together.
        for x in range(width):
            for y in range(height):
                if x + 1 < width:
                    if y + 1 < height:
                        full_graph.add_edge((x, y), (x + 1, y))
                        full_graph.add_edge((x, y), (x, y + 1))
                    else:  # lower side of the maze
                        full_graph.add_edge((x, y), (x + 1, y))
                else:
                    if y + 1 < height:  # right side of the maze
                        full_graph.add_edge((x, y), (x, y + 1))
                    else:  # lower-right corner of the maze
                        pass

        original_edges = full_graph.edges

        # At this point, the graph would form a rectangular shape. (like a chess board)
        # Now, we remove all the cycles inside the graph and initialize the new graph.
        self.edges = full_graph.spanning_tree()  # list[tuple]

        # make a deepcopy of edges
        edges_copy = deepcopy(self.edges)
        for edge in edges_copy:
            self.MazeGraph.add_edge(edge[0], edge[1])

        # stores the removed edges that would make a cycle in the maze.
        self._removed_edges = []
        for edge in original_edges:
            if not (edge in self.edges or (edge[1], edge[0]) in self.edges):
                self._removed_edges.append(edge)
        # We have chosen vertex located at (0, 0) to be the starting point
        # and vertex located at (width - 1, height - 1) to be the ending point

        for _ in range(0, self.cycles):
            random_edge = random.choice(list(self._removed_edges))
            self._removed_edges.remove(random_edge)
            v1 = random_edge[0]
            v2 = random_edge[1]
            self.edges.append((v1, v2))

    def maze_graph_to_2d_array(self) -> list[list[int]]:
        """Convert maze in a graph form into a 2-dimensional array,
        so it is easier to visualize.
        - True means it's opened -> 1
        - False means it's closed -> 0
        """
        maze_array = [[1 if (x % 2 == 1 and y % 2 == 1) else 0 for y in range(self.width * 2 + 1)]
                      for x in range(self.height * 2 + 1)]
        # Note that maze_array's index is in [x][y] order.

        # make the starting point and the ending point
        maze_array[1][0] = 1
        maze_array[self.width * 2 - 1][self.height * 2] = 1

        edges = deepcopy(self.edges)
        for edge in edges:
            point1 = edge[0]
            point2 = edge[1]
            if point1[0] == point2[0]:  # if x-coordinates are the same
                maze_array[point1[0] * 2 + 1][max(point1[1], point2[1]) * 2] = 1
            else: # if y-coordinates are the same
                maze_array[max(point1[0], point2[0]) * 2][point1[1] * 2 + 1] = 1
        return maze_array

    # def add_cycle(self, num_cycles: int) -> None:
    #     """Add a user-specified number of cycles into the Maze."""
    #     if num_cycles == 0:
    #         return
    #     for _ in range(0, num_cycles):
    #         random_edge = random.choice(list(self._removed_edges))
    #         self._removed_edges.remove(random_edge)
    #         v1 = random_edge[0]
    #         v2 = random_edge[1]
    #         self.edges.append((v1, v2))


def print_2d_array(maze: list[list[bool]]):
    """Print two-dimensional array with emojis."""
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[x][y] == 1:
                print('⬛', end="")
            else:
                print('⬜', end="")
        print()
