from collections import deque
from graph import Graph, WeightedGraph
import heapq


def breadth_first_search_traversal(graph, starting_vertex, goal_vertex=None, verbose=False):
    """
    Пребарување прво по широчина. Ова е функција која само го преминува графот и не ја зачувува патеката.
    
    :param graph: графот низ кој ќе пребаруваме
    :param starting_vertex: почетниот јазол
    :param goal_vertex: целниот јазол
    :param verbose: дали да го печати на екранот тоа што го процесира
    """
#     Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
#     Користиме листа на посетени јазли која всушност е податочна структура множество. 
#     За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
#     Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
    queue = deque([starting_vertex])
#     Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
#         Го земаме наредниот јазол за разгранување кој моментално е прв во редицата.
        vertex = queue.popleft()
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex))
#         Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph[vertex]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
#                 Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex))
#                 Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол', neighbour)
                    return
                visited.add(neighbour)
#                 Бидејќи ова е пребарување прво по широчина, соседот го додаваме на крајот од редицата јазли за разгранување.
                queue.append(neighbour)
        if verbose:
            print()


def depth_first_search_traversal(graph, starting_vertex, goal_vertex=None, verbose=False):
    """
    Пребарување прво по длабочина. Ова е функција која само го преминува графот и не ја зачувува патеката.

    :param graph: графот низ кој ќе пребаруваме
    :param starting_vertex: почетниот јазол
    :param goal_vertex: целниот јазол
    :param verbose: дали да го печати на екранот тоа што го процесира
    """
#     Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
#     Користиме листа на посетени јазли која всушност е податочна структура множество. 
#     За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
#     Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
    queue = deque([starting_vertex])
#     Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
#         Го земаме наредниот јазол за разгранување кој моментално е прв во редицата.
        vertex = queue.popleft()
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex))
#         Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph[vertex]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
#                 Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex))
#                 Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол', neighbour)
                    return
                visited.add(neighbour)
#                 Бидејќи ова е пребарување прво по длабочина, соседот го додаваме на почетокот од редицата јазли за разгранување.
                queue.appendleft(neighbour)
        if verbose:
            print()


def breadth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Пребарување прво по широчина. Ова е функција која само го преминува графот и не ја зачувува патеката.
    
    :param graph: графот низ кој ќе пребаруваме
    :param starting_vertex: почетниот јазол
    :param goal_vertex: целниот јазол
    :param verbose: дали да го печати на екранот тоа што го процесира
    :returns: патеката која е пронајдена
    """
#     Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return []
#     Користиме листа на посетени јазли која всушност е податочна структура множество. 
#     За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
#     Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
#     Тука ја памтиме и моменталната патека за секој јазол од почетниот.
    queue = deque([[starting_vertex]])
#     Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
#         Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
#         За да го земаме наредниот јазол за разгранување, ние треба од редицата да ја извадиме патеката на тој јазол.
        vertex_list = queue.popleft()
#         Јазолот за разгранување е послениот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
#         Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph[vertex_to_expand]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
#                 Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
#                 Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
#                 Бидејќи ова е пребарување прво по широчина, соседот го додаваме на крајот од редицата јазли за разгранување.
#                 Соседот го врзаме со патеката од почетниот јазол до моменталниот кој го разгрануваме.
                queue.append(vertex_list + [neighbour])
        if verbose:
            print()


def depth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Пребарување прво по длабочина. Ова е функција која само го преминува графот и не ја зачувува патеката.
    
    :param graph: графот низ кој ќе пребаруваме
    :param starting_vertex: почетниот јазол
    :param goal_vertex: целниот јазол
    :param verbose: дали да го печати на екранот тоа што го процесира
    :returns: патеката која е пронајдена
    """
#     Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
#     Користиме листа на посетени јазли која всушност е податочна структура множество. 
#     За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
#     Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
#     Тука ја памтиме и моменталната патека за секој јазол од почетниот.
    queue = deque([[starting_vertex]])
#     Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
#         Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
#         За да го земаме наредниот јазол за разгранување, ние треба од редицата да ја извадиме патеката на тој јазол.
        vertex_list = queue.popleft()
#         Јазолот за разгранување е послениот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
#         Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph[vertex_to_expand]:
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
#                 Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
#                 Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
#                 Бидејќи ова е пребарување прво по длабочина, соседот го додаваме на почетокот од редицата јазли за разгранување.
#                 Соседот го врзаме со патеката од почетниот јазол до моменталниот кој го разгрануваме.
                queue.appendleft(vertex_list + [neighbour])
        if verbose:
            print()


def uniform_cost_search(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Пребарување со униформна цена.
    
    :param graph: графот низ кој ќе пребаруваме
    :param starting_vertex: почетниот јазол
    :param goal_vertex: целниот јазол
    :param verbose: дали да го печати на екранот тоа што го процесира
    :returns: патеката која е пронајдена
    """
#     Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
#     Користиме листа на разгранети јазли која всушност е податочна структура множество. 
#     За разгранет јазол го сметаме оној јазол на кој ќе ги истражиме и процесираме неговите соседи.
    expanded = set()
#     Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
#     Тука ја памтиме и моменталната патека за секој јазол од почетниот. Дополнително, ја памтиме и цената на патот до тој момент.
#     Редицата ја преуредуваме на специјален начин така што ќе ја направиме хип структура (анг. heap).
#     Понатаму, со редицата ќе работиме само преку heapq библиотеката.
    queue = [(0, [starting_vertex])]
    heapq.heapify(queue)
#     Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
#         Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
#         За да го земаме наредниот јазол за разгранување, ние треба од редицата да ја извадиме патеката на тој јазол.
        weight, vertex_list = heapq.heappop(queue)
#         Јазолот за разгранување е послениот во оваа листа.
        vertex_to_expand = vertex_list[-1]
#         Тука ја вршиме проверката дали сме стигнале до целниот јазол 
        if vertex_to_expand == goal_vertex:
            if verbose:
                print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {} со цена {}'
                      .format(vertex_to_expand, vertex_list, weight))
            return weight, vertex_list
#         Ако веќе сме го разграниле овој јазол, нема логика да го разгрануваме пак
        if vertex_to_expand in expanded:
            if verbose:
                print('{} е веќе разгранет'.format(vertex_to_expand, weight, vertex_list))
            continue
        if verbose:
            print('Го разгрануваме јазолот {} од ({}, {})'.format(vertex_to_expand, weight, vertex_list))
#         На оваа линија код, сигурни сме дека не сме го разграниле моменталниот јазол. Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour, new_weight in graph[vertex_to_expand].items():
            if neighbour in expanded:
                if verbose:
                    print('{} е веќе разгранет'.format(neighbour))
            else:
#                 Ако моменталниот сосед не е разгранет, тогаш го додаваме во редицата на јазли за разгранување.
                if verbose:
                    print('{} со тежина {}, кој е соседен јазол на {}, го додаваме во редот за разгранување со нова '
                          'цена и го означуваме како разгранет'.format(neighbour, new_weight, vertex_to_expand))
#                 Бидејќи ова е пребарување со униформна цена, соседот кој го додаваме ќе биде соодветно среден од библиотеката heapq.
                heapq.heappush(queue, (weight + new_weight, vertex_list + [neighbour]))
#         Откако го разгранивме јазолот, го додаваме во листата разгранети јазли
        expanded.add(vertex_to_expand)
        if verbose:
            print()


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    g.add_vertex('G')
    g.add_vertex('H')
    g.add_vertex('I')
    g.add_vertex('J')
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
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_vertex('E')
    g.add_vertex('F')
    wg.add_edge(('A', 'B'), 7)
    wg.add_edge(('B', 'C'), 10)
    wg.add_edge(('A', 'C'), 9)
    wg.add_edge(('B', 'D'), 15)
    wg.add_edge(('C', 'D'), 11)
    wg.add_edge(('A', 'E'), 14)
    wg.add_edge(('C', 'E'), 2)
    wg.add_edge(('E', 'F'), 9)
    wg.add_edge(('F', 'D'), 6)

    cost, path = uniform_cost_search(wg.graph_dict, 'A', 'F', True)
    print(cost, path)
