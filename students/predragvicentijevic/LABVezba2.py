from collections import defaultdict
import heapq
from pyvis.network import Network

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


def djikstra(graph, starting_vertex, goal_vertex):
    if starting_vertex == goal_vertex:
        return
    expanded = set()
    queue = [(0, [starting_vertex])]
    heapq.heapify(queue)
    while queue:
        weight, vertex_list = heapq.heappop(queue)
        vertex_to_expand = vertex_list[-1]
        if vertex_to_expand == goal_vertex:
            return weight, vertex_list
        if vertex_to_expand in expanded:
            continue
        for neighbour, new_weight in graph[vertex_to_expand].items():
            if neighbour not in expanded:
                heapq.heappush(queue, (weight + new_weight, vertex_list + [neighbour]))
        expanded.add(vertex_to_expand)

def upload_data_and_create_graph(graph,fileToRead):
    f=open(fileToRead,"r")
    f1=f.readlines()
    for x in f1:
        a=x.split(' ')
        a[-1]=a[-1].strip()
        node=(a[0],a[1])
        weight=int(a[2])
        graph.add_edge(node,weight)

def draw_graph(e,pat):
    E1 = [x[0] for x in e]
    E2 = [x[1] for x in e]
    w = [x[2] for x in e]
    PAT = [x[0] for x in pat]
    E = E1 + E2
    E = list(dict.fromkeys(E))

    city_net = Network(height="1080px", width="1920px", font_color="black")

    edge_data = zip(E1, E2, w)
    PAT.reverse()

    if len(PAT):
        prvo = PAT.pop()
        if len(PAT):
            vtoro = PAT.pop()

    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]

        if src == prvo and dst == vtoro and len(PAT) != 0:
            city_net.add_node(src, src, title=src, color="#00ff1e")
            city_net.add_node(dst, dst, title=dst, color="#00ff1e")
            city_net.add_edge(src, dst, value=w, color="#00ff1e")
            if len(PAT):
                prvo = PAT.pop()
                if len(PAT):
                    vtoro = PAT.pop()

        else:
            city_net.add_node(src, src, title=src)
            city_net.add_node(dst, dst, title=dst)
            city_net.add_edge(src, dst, value=w)

    neighbor_map = city_net.get_adj_list()

    for node in city_net.nodes:
        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
        node["value"] = len(neighbor_map[node["id"]])

    city_net.show("mygraph.html")

graph=WeightedGraph()
upload_data_and_create_graph(graph,"distances.txt")
cena, pat = djikstra(graph.graph_dict,'SU','KO')
print(cena)
print(pat)
draw_graph(graph.edges(),pat)