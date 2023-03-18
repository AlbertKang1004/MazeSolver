"""CSC111 Group Project: Maze Solver

Group Members:
    - Vihaas Chugh
    - Aria Coventry
    - Albert Kang
    - Abhishek Sharma

This file contains a basic Graph implementation, for future use."""

from __future__ import annotations
# from python_ta.contracts import check_contracts
import random


# @check_contracts
class Graph:
    """A graph that is used to represent the maze.

    Private Instance Attributes:
        - _vertices:
             A collection of the vertices contained in this graph.
             Maps item to _Vertex object.

    Instance Attributes:
        - edges:
            A list of edges.

    """
    _vertices: dict[tuple[int, int], _Vertex]
    edges: set[tuple[tuple, tuple]]

    def __init__(self) -> None:
        self._vertices = {}
        self.edges = set()

    def add_vertex(self, x: int, y: int) -> None:
        """Add a vertex with the given co-ordinates to this graph.
        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
            - 0 <= loc[0] < self.width
            - 0 <= loc[1] < self.height
        """
        new_vertex = _Vertex((x, y), set())
        self._vertices[(x, y)] = new_vertex

    def add_edge(self, loc1: tuple[int, int], loc2: tuple[int, int]) -> None:
        """Add an edge between the two vertices with the given coordinates in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - loc1 != loc2
            -
        """
        if loc1 in self._vertices and loc2 in self._vertices:
            # Add the edge between the two vertices
            v1 = self._vertices[loc1]
            v2 = self._vertices[loc2]

            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
            edge = (v1.loc, v2.loc)
            self.edges.add(edge)
        else:
            raise ValueError

    def spanning_tree(self) -> list[set[tuple[int, int]]]:
        """Return a subset of the edges of this graph that form a spanning tree.

        The edges are returned as a list of sets, where each set contains the two
        COORDINATES corresponding to an edge. Each returned edge is in this graph
        (i.e., this function doesn't create new edges!).

        Preconditions:
            - this graph is connected
        """
        # How do we choose the starting vertex?
        all_vertices = list(self._vertices.values())
        start_vertex = random.choice(all_vertices)  # Could also use random.choice(all_vertices)

        return start_vertex.get_spanning_tree(set())


# @check_contracts
class _Vertex:
    """A vertex in the MazeGraph.

    Instance Attributes:

        - loc: The coordinates of the vertex, represented as a tuple of (x, y) form
        - neighbours: The vertices that are connected to this vertex

    Representation Invaritants:
        - loc[0] > 0 and loc[1] > 0
    """
    loc: tuple[int, int]
    neighbours: set[_Vertex]

    def __init__(self, loc: tuple[int, int], neighbours: set[_Vertex]):
        self.loc = loc
        self.neighbours = neighbours

    def get_spanning_tree(self, visited: set[_Vertex]) -> list[tuple]:
        """Return a spanning tree for all items this vertex is connected to,
        without using any of the vertices in visited

        Preconditions:
            - self not in visited
        """
        visited.add(self)

        edges_so_far = []

        for u in self.neighbours:
            if u not in visited:
                edges_so_far.append((self.loc, u.loc))
                edges_so_far.extend(u.get_spanning_tree(visited))

        return edges_so_far
