"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaas Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a maze class, which includes various fundcions."""

import random
from copy import deepcopy
from graph import Graph
# from python_ta.contracts import check_contracts

index = tuple[int, int]


# @check_contracts
class Maze:
    """A Maze represented in a graph.

    Instance Attributes:
        - width: the width of the maze
        - height: the height of the maze
        - maze_graph: the graph representation of maze
        - edges: the edges that this graph have
        - cycles: number of cycles in the maze

    Private Instance Attributes:
        - _removed_edges: stores the edge that was removed when a graph transformed into a spanning tree.
                          Needed for adding cycles in a maze.

    Representation Invariants:
        - self.width >= 3 and self.height >= 3
        - cycles >= 0
    """
    width: int
    height: int
    maze_graph: Graph
    edges: list[tuple]
    cycles: int
    _removed_edges: list[tuple]

    def __init__(self, width: int, height: int, cycles: int = 0) -> None:
        """Initialize a maze with a specified width and height."""
        self.width = width
        self.height = height
        self.cycles = cycles
        self.maze_graph = Graph()
        # First, initialize all the vertices.
        full_graph = Graph()
        for x in range(width):
            for y in range(height):
                full_graph.add_vertex(x, y)
                self.maze_graph.add_vertex(x, y)

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
        full_graph.remove_edge((width - 2, height - 1), (width - 1, height - 1))
        # We want to remove one of the two paths connected to the endpoint of the maze.

        original_edges = full_graph.edges
        # At this point, the graph would form a rectangular shape. (like a chess board)
        # Now, we remove all the cycles inside the graph and initialize the new graph.

        self.edges = full_graph.spanning_tree()  # list[tuple]

        # make a deepcopy of edges
        edges_copy = deepcopy(self.edges)
        for edge in edges_copy:
            self.maze_graph.add_edge(edge[0], edge[1])

        # stores the removed edges that would make a cycle in the maze.
        self._removed_edges = []
        for edge in original_edges:
            if not (edge in self.edges or (edge[1], edge[0]) in self.edges):
                self._removed_edges.append(edge)

        # We have chosen vertex located at (0, 0) to be the starting point
        # and vertex located at (width - 1, height - 1) to be the ending point
        for _ in range(self.cycles):
            random_edge = random.choice(list(self._removed_edges))
            self._removed_edges.remove(random_edge)
            self.maze_graph.add_edge(random_edge[0], random_edge[1])
            self.edges.append(random_edge)

    def find_solution(self) -> list[index]:
        """Return the shortest path of the graph."""
        return self.maze_graph.bfs((0, 0), (self.width - 1, self.height - 1))

    def maze_graph_to_2d_array(self, show_solution: bool = False) -> list[list[int]]:
        """Convert maze in a graph form into a 2-dimensional array,
        so it is easier to visualize.
            - 0 means it's closed
            - 1 means it's opened
            - 2 means it's used to display the path of the shortest solution

        - If show_solution is not specified or False, it will not display the solution when printing out the maze.
        - If show_solution is True, it will show the shortest solution with brown squares.
        """
        maze_array = [[1 if (x % 2 == 1 and y % 2 == 1) else 0 for y in range(self.height * 2 + 1)]
                      for x in range(self.width * 2 + 1)]
        # Note that maze_array's index is in [x][y] order.

        # make the starting point and the ending point
        maze_array[1][0] = 1
        maze_array[-2][-1] = 1

        edges = deepcopy(self.edges)
        for edge in edges:
            x1, y1 = edge[0]
            x2, y2 = edge[1]
            if x1 == x2:  # if x-coordinates are the same
                maze_array[x1 * 2 + 1][max(y1, y2) * 2] = 1
            else:  # if y-coordinates are the same
                maze_array[max(x1, x2) * 2][y1 * 2 + 1] = 1

        if show_solution:
            path = self.find_solution()

            maze_array[1][0] = 2  # Starting point
            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                maze_array[x1 * 2 + 1][y1 * 2 + 1] = 2
                maze_array[x1 + x2 + 1][y1 + y2 + 1] = 2
            maze_array[-2][-2] = 2  # Leftover case
            maze_array[-2][-1] = 2  # Ending point
        return maze_array


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['random', 'copy', 'graph'],
        'allowed-io': [],
        'disable': ['E9992', 'E9997', 'E9998']
    })
