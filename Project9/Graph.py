import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a Vertex id to the path.
            :param vertex: The id of the vertex to be added
            :return: None
            """
            if vertex is None:
                return
            self.vertices.append(vertex)

        def remove_vertex(self):
            """
            Remove the most recently added Vertex id from the path.
            :return: None
            """
            if self.is_empty() is True:
                return
            self.vertices.pop(-1)

        def last_vertex(self):
            """
            Return the last Vertex id added to the path
            :return: None if path is empty, the last vertex otherwise
            """
            if self.is_empty() is True:
                return
            return self.vertices[-1]

        def is_empty(self):
            """
            Check if the path is empty.
            :return: True if vertices is empty, False otherwise
            """
            return len(self.vertices) == 0

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Add an edge to the Vertex given the id of the destination Vertex.
            :param destination: The id of the vertex that is the destination of the edge to be added
            :return: None
            """
            if destination is None:
                return
            ed = Graph.Edge(self, destination)
            self.edges.append(ed)

        def degree(self):
            """
            Return the number of outgoing edges (degree) of the Vertex
            :return: length of edges
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Returns the Edge that goes to a specified destination node.
            :param destination: the destination of the desired edge
            :return: None if the edge is not found, the edge otherwise
            """
            if destination is None:
                return
            i = 0
            while i < len(self.edges):
                if self.edges[i].destination == destination:
                    return self.edges[i]
                i += 1
            return None

        def get_edges(self):
            """
            Returns a list of all of the edges.
            :return: A list of all the edges in this vertex
            """
            return self.edges

        def set_fake(self):
            """
            Set the vertex as a fake vertex.
            :return: None
            """
            self.fake = True

        def visit(self):
            """
            Set the vertex as visited.
            :return: None
            """
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        Returns the vertex with the specified id.
        :param ID: The ID of the desired vertex
        :return: None if the vertex is not found, the vertex otherwise
        """
        return self.adj_list.get(ID)

    def construct_graph(self):
        """
        Add all edges to a Graph. If a filename is provided,
        read from the file to construct the graph and disregard
        the size and connectedness, otherwise use the generate_edges
        method to construct the graph. Do not accept graphs with a
        size less than or equal to 0 or connectedness not in the range (0, 1]
        :return: None
        """
        if self.connectedness > 1 or self.connectedness < 0:
            raise GraphError
        if self.size < 0:
            raise GraphError
        elif self.filename is None and self.size > 0:
            gen = self.generate_edges()
            data = []
            for i in gen:
                data.append((i[0], i[1]))
            for i in data:
                if i[0] not in self.adj_list.keys():
                    vert1 = self.Vertex(i[0])
                    self.adj_list[vert1.ID] = vert1
                if i[1] not in self.adj_list.keys():
                    vert2 = self.Vertex(i[1])
                    self.adj_list[vert2.ID] = vert2
                if self.adj_list[i[0]].get_edge(i[1]) is None:
                    self.adj_list[i[0]].add_edge(i[1])
            if data[-1][0] is not self.size - 1:
                vert = self.Vertex(self.size-1)
                self.adj_list[vert.ID] = vert
        elif self.filename is not None:
            file = open(self.filename, 'r')
            read = []
            for i in file:
                lineformat = i.strip('\n').split()
                read.append((int(lineformat[0]), int(lineformat[1])))
            for i in read:
                if i[0] not in self.adj_list.keys():
                    vert1 = self.Vertex(i[0])
                    self.adj_list[vert1.ID] = vert1
                if i[1] not in self.adj_list.keys():
                    vert2 = self.Vertex(i[1])
                    self.adj_list[vert2.ID] = vert2
                if self.adj_list[i[0]].get_edge(i[1]) is None:
                    self.adj_list[i[0]].add_edge(i[1])
        else:
            raise GraphError

    def BFS(self, start, target):
        """
        Breadth First Search given a start ID, find a path to the target ID.
        :param start: The ID of the vertex to start the search from
        :param target: The ID of the desired end vertex
        :return: A path between start and target
        """
        stack = [Graph.Path([start])]
        while stack:
            path = stack.pop(0)
            vert = self.get_vertex(path.last_vertex())
            if vert.ID == target:
                return path
            for i in vert.get_edges():
                new_path = self.Path(path.vertices[:])
                new_path.add_vertex(i.destination)
                stack.append(new_path)
        return Graph.Path()

    def DFS(self, start, target, path=Path()):
        """
        Depth First Search given a start ID, find a path to the target ID.
        :param start: The ID of the vertex to start the search from
        :param target: The ID of the desired vertex
        :param path: The path between start and another vertex, not necessarily target
        :return: A path between start and target
        """
        if self.get_vertex(start) is None or self.get_vertex(target) is None:
            return Graph.Path()
        if len(self.adj_list) == 0:
            return Graph.Path()
        path.add_vertex(start)
        if start == target:
            return path
        vert = self.get_vertex(start)
        vert.visit()
        edges = vert.get_edges()
        dest = None
        j = 0
        while j < vert.degree():
            if self.adj_list.get(edges[j].destination).visited is False:
                dest = edges[j].destination
                j = vert.degree()
            j += 1
        if dest is None:
            path.remove_vertex()
            st = path.last_vertex()
            path.remove_vertex()
            return self.DFS(st, target, path)
        else:
            return self.DFS(dest, target, path)


def fake_emails(graph, mark_fake=False):
    """
    Finds all fake vertices in the Graph, sets them to be fake,
    and adds their IDs to a list. A Vertex is fake if the degree
    of the vertex is 0 (messages coming in, no messages going out).
    :param graph: The graph to find the fake emails in
    :param mark_fake: If True, marks emails as fake, otherwise doesn't mark the emails
    :return: The list of fake emails
    """
    def check_fake_emails(start, emails=list()):
        """
        Given a start Vertex ID, find all fake email addressses that can
        be reached from that ID and remove the edge connecting to the fake address
        :param start: The vertex ID to start the search for fake emails from
        :param emails: The list of fake emails
        :return: A list of fake emails
        """
        vert = graph.get_vertex(start)
        vert.visit()
        edges = vert.get_edges()
        if vert.degree() == 0 and mark_fake is True:
            vert.set_fake()
            emails.append(vert.ID)
        j = 0
        while j < len(edges):
            if j >= len(edges):
                break
            if graph.get_vertex(edges[j].destination).visited is False:
                check_fake_emails(edges[j].destination, emails)
            if graph.get_vertex(edges[j].destination).fake is True:
                edges.pop(j)
                j -= 1
            j += 1
        return emails
    fake = []
    for i in graph.adj_list:
        if graph.get_vertex(i).visited is False:
            fake = check_fake_emails(i, fake)
    return fake
