from collections import defaultdict


class Graph():
    """
    Ова е класата за граф која претставува интерфејс за користење на податочаната структура речник преку терминологија за графови.
    """
    def __init__(self):
        """
        Иницијалицираме празен речник што претставува празен граф.
        """
        self.graph_dict = {}

    def vertices(self):
        """
        Јазлите се складирано како клучеви на речникот.
        """
        return list(self.graph_dict.keys())

    def edges(self):
        """
        Правиме листа од сите врски во графот. 
        Соседите на еден јазол се сместени во листа која се наоѓа во речникот каде клуч е самиот јазол.
        На излезот ја враќаме листа каде секоја врска е претставена како торка од 2 елементи.
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges

    def add_vertex(self, vertex):
        """
        Додава јазол во графот. Клуч е самиот јазол, а вредноста е празна листа бидејќи тој јазол сѐ уште нема соседи.
        :vertex: е јазолот кој треба да го додадаме.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge, add_reversed=True):
        """
        Додава врска во графот. Првиот член во торката edge е клуч, а во неговата листа во речникот се додава вториот член од торката.
        :edge: е торка од 2 елементи кои ја претставуваат врската која треба да се додаде во графот.
        :add_reversed: е логичка променлива која, доколку е логичка единица, ќе ја додаде и обратната врска во графот.
        """
        vertex1, vertex2 = edge
        self.graph_dict[vertex1].append(vertex2)
        if add_reversed:
            self.graph_dict[vertex2].append(vertex1)

    def remove_vertex(self, vertex_to_remove):
        """
        Отстранува јазол од графот. Прво се отстранува вредноста во речникот каде клуч е самиот јазол. 
        Потоа јазолот се отстранува од листата на секој јазол во графот.
        :vertex_to_remove: е јазолот кој треба да се отсрани.
        """
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                self.graph_dict[vertex].remove(vertex_to_remove)

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        """
        Отстранува врска од графот. Тоа се изведува преку бришење на вториот јазол на торката edge_to_remove 
        од листата на првиот јазол на торката edge_to_remove.
        :edge_to_remove: е врската која треба да биде избришана.
        :remove_reversed: е логичка променлива која, доколку е логичка единица, ќе ја избрише и обратна врска.
        """
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)

    def isolated_vertices(self):
        """
        Ги наоѓа изолираните јазли. Тоа се јазлите кои имаат празна листа во речникот.
        """
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def __str__(self):
        """
        Ова е функција за подобро печатење на графот кога ќе повикаме print(graph)
        """
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())


class WeightedGraph(object):
    """
    Ова е класата за тежински граф која претставува интерфејс за користење на податочаната структура речник преку терминологија за графови.
    """
    def __init__(self):
        """
        Иницијалицираме празен речник што претставува празен граф. Секоја вреднност на речникот е друг речник. 
        Како вредности на вторите речници се тежините на секоја врска.
        """
        self.graph_dict = defaultdict(dict)

    def vertices(self):
        """
        Јазлите се складирано како клучеви на речникот.
        """
        return list(self.graph_dict.keys())

    def edges(self):
        """
        Правиме листа од сите врски во графот.
        Соседите на еден јазол се сместени во речник кој се наоѓа во речникот каде клуч е самиот јазол.
        На излезот ја враќаме листата каде секоја врска е претставена како торка од 3 елементи, вклучувајќи ја и тежината на врската.
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour, weight in self.graph_dict[vertex].items():
                edges.append((vertex, neighbour, weight))
        return edges

    def add_vertex(self, vertex):
        """
        Додава јазол во графот. Клуч е самиот јазол, а вредноста е празен речник бидејќи тој јазол сѐ уште нема соседи.
        :vertex: е јазолот кој треба да го додадаме.
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}

    def add_edge(self, edge, weight, add_reversed=True):
        """
        Додава врска во графот. Првиот член во торката edge е клуч, а во неговиот речник во главниот речник се додава вториот член од торката.
        :edge: е торка од 2 елементи кои ја претставуваат врската која треба да се додаде во графот.
        :weight: е тежина на врската
        :add_reversed: е логичка променлива која, доколку е логичка единица, ќе ја додаде и обратната врска во графот.
        """
        vertex1, vertex2 = edge
        self.graph_dict[vertex1][vertex2] = weight
        if add_reversed:
            self.graph_dict[vertex2][vertex1] = weight

    def remove_vertex(self, vertex_to_remove):
        """
        Отстранува јазол од графот. Прво се отстранува вредноста во речникот каде клуч е самиот јазол. 
        Потоа јазолот се отстранува од речниците на секој јазол во графот.
        :vertex_to_remove: е јазолот кој треба да се отсрани.
        """
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                del self.graph_dict[vertex][vertex_to_remove]

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        """
        Отстранува врска од графот. Тоа се изведува преку бришење на вториот јазол на торката edge_to_remove 
        од речникот на првиот јазол на торката edge_to_remove.
        :edge_to_remove: е врската која треба да биде избришана.
        :remove_reversed: е логичка променлива која, доколку е логичка единица, ќе ја избрише и обратна врска.
        """
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            del self.graph_dict[vertex1][vertex2]
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                del self.graph_dict[vertex2][vertex1]

    def isolated_vertices(self):
        """
        Ги наоѓа изолираните јазли. Тоа се јазлите кои имаат празен речник во главниот речник речникот.
        """
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def __str__(self):
        return 'Vertices: {}\nEdges: {}'.format(self.vertices(), self.edges())
