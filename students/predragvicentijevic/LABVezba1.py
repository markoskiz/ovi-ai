from collections import defaultdict
from collections import deque
from pyvis.network import Network

class Graph(object):
    def __init__(self, graph_dict=defaultdict(list)):
        self.graph_dict = graph_dict

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

    def add_edge(self, edge, add_reversed=True):
        vertex1, vertex2 = edge
        self.graph_dict[vertex1].append(vertex2)
        if add_reversed:
            self.graph_dict[vertex2].append(vertex1)

    def remove_vertex(self, vertex_to_remove):
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                self.graph_dict[vertex].remove(vertex_to_remove)

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)

    def isolated_vertices(self):
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def __str__(self):
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())

    def neighbours(self,vertex):
        return self.graph_dict[vertex]



def breadth_first_search_find_path(graph, starting_vertex, goal_vertex):

    if starting_vertex == goal_vertex:
        return []
    visited = {starting_vertex}
    queue = deque([[starting_vertex]])
    while queue:
        vertex_list = queue.popleft()
        vertex_to_expand = vertex_list[-1]
        for neighbour in graph.neighbours(vertex_to_expand):
            if neighbour not in visited:
                if neighbour == goal_vertex:
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                queue.append(vertex_list + [neighbour])

def generate_Graph_and_search(graph, Xn, Yn, Zn, C1, C2, C3):
    start_node=(Xn,Yn,Zn)
    graph.add_vertex(start_node)
    if Xn==1:
        return start_node

    poseteni={start_node}
    navigator=deque([start_node])

    while navigator:
        nav = navigator.popleft()
        Xn, Yn, Zn = nav

        if Yn < C2:
            if (C2 - Yn) >= Xn:
                node = (0, Yn + Xn, Zn)
            elif (C2 - Yn) < Xn:
                node = (Xn - (C2 - Yn), Yn + (C2 - Yn), Zn)
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn < C3:
            if (C3 - Zn) >= Xn:
                node = (0, Yn, Zn + Xn)
            elif (C3 - Zn) < Xn:
                node = (Xn - (C3 - Zn), Yn, Zn + (C3 - Zn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Xn != 0:
            node = (0, Yn, Zn)
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Xn != C1:
            node = (C1, Yn, Zn)
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

        if Xn < C1:
            if (C1 - Xn) >= Yn:
                node = (Yn + Xn, 0, Zn)
                if node==(1,0,0):
                    break
            elif (C1 - Xn) < Yn:
                node = (Xn + (C1 - Xn), Yn - (C1 - Xn), Zn)
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn < C3:
            if (C3 - Zn) >= Yn:
                node = (Xn, 0, Zn + Yn)
            elif (C3 - Zn) < Yn:
                node = (Xn, Yn - (C3 - Zn), Zn + (C3 - Zn))
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn != 0:
            node = (Xn, 0, Zn)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn != C2:
            node = (Xn, C2, Zn)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

        if Xn < C1:
            if (C1 - Xn) >= Zn:
                node = (Xn + Zn, Yn, 0)
                if node==(1,0,0):
                    break
            elif (C1 - Xn) < Zn:
                node = (Xn + (C1 - Xn), Yn, Zn - (C1 - Xn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Yn < C2:
            if (C2 - Yn) >= Zn:
                node = (Xn, Yn + Zn, 0)
                if node==(1,0,0):
                    break
            elif (C2 - Yn) < Zn:
                node = (Xn, Yn + (C2 - Yn), Zn - (C2 - Yn))
                if node==(1,0,0):
                    break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn != 0:
            node = (Xn, Yn, 0)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)
        if Zn != C3:
            node = (Xn, Yn, C3)
            if node==(1,0,0):
                break
            if node not in poseteni:
                poseteni.add(node)
                graph.add_vertex(node)
                graph.add_edge((node, nav))
                navigator.append(node)

    if node not in poseteni:
        poseteni.add(node)
        graph.add_vertex(node)
        graph.add_edge((node, nav))
        navigator.append(node)
    fastest_path=breadth_first_search_find_path(graph,start_node,(1,0,0))
    return fastest_path

def draw_graph(e,pat):
    e1 = [x[0] for x in e]
    e2 = [x[1] for x in e]

    e = e1 + e2
    e = list(dict.fromkeys(e))

    E1 = []
    for i in e1:
        E1.append(str(i))
    E2 = []
    for i in e2:
        E2.append(str(i))
    E = []
    for i in e:
        E.append(str(i))
    PAT = []
    for i in pat:
        PAT.append(str(i))
    water_net = Network(height="1080px", width="1920px", font_color="black")

    w = [1 for i in range(len(E1))]

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
            water_net.add_node(src, src, title=src, color="#00ff1e")
            water_net.add_node(dst, dst, title=dst, color="#00ff1e")
            water_net.add_edge(src, dst, value=w, color="#00ff1e")
            if len(PAT):
                prvo = PAT.pop()
                if len(PAT):
                    vtoro = PAT.pop()

        else:
            water_net.add_node(src, src, title=src)
            water_net.add_node(dst, dst, title=dst)
            water_net.add_edge(src, dst, value=w)

    neighbor_map = water_net.get_adj_list()

    for node in water_net.nodes:
        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
        node["value"] = len(neighbor_map[node["id"]])

    water_net.show("mygraph.html")

graph=Graph()
c1=5
c2=8
c3=10
x=0
y=0
z=0
listazapat=generate_Graph_and_search(graph,x,y,z,c1,c2,c3)
print(listazapat)
draw_graph(graph.edges(),listazapat)


