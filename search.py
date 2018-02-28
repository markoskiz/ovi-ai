from collections import deque
from graph import Graph, WeightedGraph
import heapq


def breadth_first_search_traversal(graph, starting_vertex, goal_vertex=None, verbose=False):
    """
    Breadth first search algorithm
    
    :param graph: graph dictionary to traverse
    :param starting_vertex: vertext to start from
    :param goal_vertex: vertex to look for
    :param verbose: True for debug options
    :return: None
    """
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    visited = {starting_vertex}
    queue = deque([starting_vertex])
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        vertex = queue.popleft()
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex))
        for neighbour in graph[vertex]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex))
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол', neighbour)
                    return
                visited.add(neighbour)
                queue.append(neighbour)
        if verbose:
            print()


def depth_first_search_traversal(graph, starting_vertex, goal_vertex=None, verbose=False):
    """
    Depth first search algorithm

    :param graph: graph dictionary to traverse
    :param starting_vertex: vertext to start from
    :param goal_vertex: vertex to look for
    :param verbose: True for debug options
    :return: None
    """
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    visited = {starting_vertex}
    queue = deque([starting_vertex])
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        vertex = queue.popleft()
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex))
        for neighbour in graph[vertex]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex))
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол', neighbour)
                    return
                visited.add(neighbour)
                queue.appendleft(neighbour)
        if verbose:
            print()


def breadth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Breadth first search algorithm with recorded path from starting vertex to goal vertex

    :param graph: graph dictionary to traverse
    :param starting_vertex: vertext to start from
    :param goal_vertex: vertex to look for
    :param verbose: True for debug options
    :returns: path from starting vertex to goal vertex
    """
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return []
    visited = {starting_vertex}
    queue = deque([[starting_vertex]])
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        vertex_list = queue.popleft()
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
        for neighbour in graph[vertex_to_expand]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                queue.append(vertex_list + [neighbour])
        if verbose:
            print()


def depth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Depth first search algorithm with recorded path from starting vertex to goal vertex

    :param graph: graph dictionary to traverse
    :param starting_vertex: vertext to start from
    :param goal_vertex: vertex to look for
    :param verbose: True for debug options
    :returns: path from starting vertex to goal vertex
    """
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    visited = {starting_vertex}
    queue = deque([[starting_vertex]])
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        vertex_list = queue.popleft()
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
        for neighbour in graph[vertex_to_expand]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                queue.appendleft(vertex_list + [neighbour])
        if verbose:
            print()


def djikstra(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Djikstra's algorithm

    :param graph: graph dictionary to traverse
    :param starting_vertex: vertext to start from
    :param goal_vertex: vertex to look for
    :param verbose: True for debug options
    :returns: optimal path from starting vertex to goal vertex
    """
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    expanded = set()
    queue = [(0, [starting_vertex])]
    heapq.heapify(queue)
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        weight, vertex_list = heapq.heappop(queue)
        vertex_to_expand = vertex_list[-1]
        if vertex_to_expand == goal_vertex:
            if verbose:
                print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {} со цена {}'
                      .format(vertex_to_expand, vertex_list, weight))
            return weight, vertex_list
        if vertex_to_expand in expanded:
            if verbose:
                print('{} е веќе разгранет'.format(vertex_to_expand, weight, vertex_list))
            continue
        if verbose:
            print('Го разгрануваме јазолот {} од ({}, {})'.format(vertex_to_expand, weight, vertex_list))
        for neighbour, new_weight in graph[vertex_to_expand].items():
            if neighbour in expanded:
                if verbose:
                    print('{} е веќе разгранет'.format(neighbour))
            else:
                if verbose:
                    print('{} со тежина {}, кој е соседен јазол на {}, го додаваме во редот за разгранување со нова '
                          'цена и го означуваме како разгранет'.format(neighbour, new_weight, vertex_to_expand))
                heapq.heappush(queue, (weight + new_weight, vertex_list + [neighbour]))
        expanded.add(vertex_to_expand)
        if verbose:
            print()


if __name__ == '__main__':
    g = Graph()
    g.add_edge(('A', 'B'))
    g.add_edge(('B', 'C'))
    g.add_edge(('C', 'D'))
    g.add_edge(('D', 'E'))
    g.add_edge(('E', 'F'))
    g.add_edge(('F', 'G'))
    g.add_edge(('G', 'H'))
    g.add_edge(('H', 'I'))
    g.add_edge(('I', 'J'))
    g.add_edge(('J', 'A'))
    g.add_edge(('C', 'H'))

    depth_first_search_traversal(graph=g.graph_dict, starting_vertex='A', goal_vertex='F', verbose=True)

    path = breadth_first_search_find_path(graph=g.graph_dict, starting_vertex='A', goal_vertex='F', verbose=True)
    print(path)

    wg = WeightedGraph()
    wg.add_edge(('A', 'B'), 7)
    wg.add_edge(('B', 'C'), 10)
    wg.add_edge(('A', 'C'), 9)
    wg.add_edge(('B', 'D'), 15)
    wg.add_edge(('C', 'D'), 11)
    wg.add_edge(('A', 'E'), 14)
    wg.add_edge(('C', 'E'), 2)
    wg.add_edge(('E', 'F'), 9)
    wg.add_edge(('F', 'D'), 6)

    cost, path = djikstra(wg.graph_dict, 'A', 'F', True)
    print(cost, path)
