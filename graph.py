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

index = tuple[int, int]


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
    _vertices: dict[index, _Vertex]
    edges: set[tuple[index, index]]

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

    def add_edge(self, loc1: index, loc2: index) -> None:
        """Add an edge between the two vertices with the given coordinates in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - loc1 != loc2
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

    def remove_edge(self, loc1: index, loc2: index) -> None:
        """remove edge located between two indices."""
        v1 = self._vertices[loc1]
        v2 = self._vertices[loc2]
        if (loc1, loc2) in self.edges or (loc2, loc1) in self.edges:
            if (loc1, loc2) in self.edges:
                self.edges.remove((loc1, loc2))
            else:
                self.edges.remove((loc2, loc1))
            v1.neighbours.remove(v2)
            v2.neighbours.remove(v1)
        else:
            raise ValueError

    def spanning_tree(self) -> list[index]:
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

    def get_graph_dictionary(self) -> dict[index, list[index]]:
        """Return the dictionary version of the graph.
        This function is very important for the Breath-First Search Algorithm.
        """
        return {nodes: [neighbour.loc for neighbour in self._vertices[nodes].neighbours]
                for nodes in self._vertices}

    def bfs(self, start: index, end: index) -> list[index]:
        """Return the shortest solution for the graph, using the Breadth-First Search.

        Note that the maze we made will have top-left node as a starting point,
        and bottom-right node as an ending point.
        """

        visited = []
        queue = [[start]]

        if start == end:
            return []

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbours = self.get_graph_dictionary()[node]

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == end:
                        return new_path

                visited.append(node)

        raise AssertionError
        # This code should be unreachable as maze's starting point and ending point is connected


# @check_contracts
class _Vertex:
    """A vertex in the MazeGraph.

    Instance Attributes:
        - loc: The coordinates of the vertex, represented as a tuple of (x, y) form
        - neighbours: Vertices that are connected to this vertex.

    Representation Invaritants:
        - loc[0] >= 0 and loc[1] >= 0
    """
    loc: index
    neighbours: set[_Vertex]

    def __init__(self, loc: index, neighbours: set[_Vertex]) -> None:
        self.loc = loc
        self.neighbours = neighbours

    def get_spanning_tree(self, visited: set[_Vertex]) -> list[tuple]:
        """Return a spanning tree for all items this vertex is connected to,
        without using any of the vertices in visited.

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


if __name__ == '__main__':
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run PythonTA,
    # and then also test your methods manually in the console.
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'max-nested-blocks': 4,
        'extra-imports': ['random'],
        'allowed-io': [],
        'disable': ['E9992', 'E9997']
    })
