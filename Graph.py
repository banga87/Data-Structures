from Vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex
    
    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph_dict[from_vertex].add_edge(to_vertex, weight)
        if not self.directed:
            self.graph_dict[to_vertex].add_edge(from_vertex, weight)