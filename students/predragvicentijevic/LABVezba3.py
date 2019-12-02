from collections import defaultdict
import heapq
import math

class WeightedGraph(object):
    def __init__(self):
        self.graph_dict = defaultdict(dict)

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbour, weight in self.graph_dict[vertex].items():
                edges.append((vertex, neighbour, weight))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}

    def add_edge(self, edge, weight, add_reversed=True):
        vertex1, vertex2 = edge
        self.graph_dict[vertex1][vertex2] = weight
        if add_reversed:
            self.graph_dict[vertex2][vertex1] = weight

    def remove_vertex(self, vertex_to_remove):
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                del self.graph_dict[vertex][vertex_to_remove]

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            del self.graph_dict[vertex1][vertex2]
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                del self.graph_dict[vertex2][vertex1]

    def isolated_vertices(self):
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def __str__(self):
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())






def A_Star(graph, starting_vertex, goal_vertex,eristics):
    if starting_vertex == goal_vertex:
        return
    for i in eristics:
        baranJazol, sirina1, dolzina1 = i
        if baranJazol == goal_vertex:
            break
    expanded = set()
    queue = [(0, [starting_vertex])]
    heapq.heapify(queue)
    while queue:
        weight, vertex_list = heapq.heappop(queue)
        vertex_to_expand = vertex_list[-1]

        for i in eristics:
            jazol, sirina, dolzina = i
            if jazol==vertex_to_expand:
                weight+=distance_on_unit_sphere(sirina,dolzina,sirina1,dolzina1)
                break

        if vertex_to_expand == goal_vertex:
            return weight, vertex_list
        if vertex_to_expand in expanded:
            continue
        for neighbour, new_weight in graph[vertex_to_expand].items():
            if neighbour not in expanded:
                heapq.heappush(queue, (weight + new_weight, vertex_list + [neighbour]))
        expanded.add(vertex_to_expand)


def distance_on_unit_sphere(lat1, long1, lat2, long2):
    degrees_to_radians = math.pi / 180.0
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians
    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)
    return arc

def upload_data_and_create_graph(graph,fileToRead):
    f=open(fileToRead,"r")
    f1=f.readlines()
    for x in f1:
        a=x.split(' ')
        a[-1]=a[-1].strip()
        edge=(a[0],a[1])
        weight=float(a[2])
        graph.add_edge(edge,weight)

def add_locations(graph,fileToRead):
    f = open(fileToRead, "r")
    f1 = f.readlines()
    lokacii=[]
    for x in f1:
        a=x.split(' ')
        a[-1]=a[-1].strip()
        node=a[0]
        lat=float(a[1])
        lon=float(a[2])
        lokacii.append((node,lat,lon))
    return lokacii



graph = WeightedGraph()
upload_data_and_create_graph(graph,"distances.txt")
lokacii=add_locations(graph,"locations.txt")
cena, pat = A_Star(graph.graph_dict,"SU","KO",lokacii)
print(cena)
print(pat)

