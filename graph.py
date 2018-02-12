from collections import defaultdict


class Graph(object):
    def __init__(self, graph_dict=None):
        self.graph_dict = defaultdict(list) if graph_dict is None else graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge, add_reversed=False):
        vertex1, vertex2 = edge
        self.graph_dict[vertex1].append(vertex2)
        if add_reversed:
            self.graph_dict[vertex2].append(vertex1)

    def remove_vertex(self, vertex_to_remove):
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                self.graph_dict[vertex].remove(vertex_to_remove)

    def remove_edge(self, edge_to_remove, remove_reversed=False):
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)

    def __str__(self):
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())
