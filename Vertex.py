from unittest.loader import VALID_MODULE_NAME


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return self.edges.keys()

    def add_edge(self, vertex, weight):
        self.edges[vertex] = weight