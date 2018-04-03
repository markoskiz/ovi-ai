import math
from graph import Graph

g = Graph()

g.add_edge(('A', 'B'), add_reversed=False)
g.add_edge(('A', 'C'), add_reversed=False)
g.add_edge(('A', 'D'), add_reversed=False)
g.add_edge(('B', 'E'), add_reversed=False)
g.add_edge(('B', 'F'), add_reversed=False)
g.add_edge(('C', 'G'), add_reversed=False)
g.add_edge(('C', 'H'), add_reversed=False)
g.add_edge(('D', 'I'), add_reversed=False)
g.add_edge(('D', 'J'), add_reversed=False)
g.add_edge(('E', 'K'), add_reversed=False)
g.add_edge(('E', 'L'), add_reversed=False)
g.add_edge(('F', 'M'), add_reversed=False)
g.add_edge(('F', 'N'), add_reversed=False)
g.add_edge(('G', 'O'), add_reversed=False)
g.add_edge(('G', 'P'), add_reversed=False)
g.add_edge(('H', 'Q'), add_reversed=False)
g.add_edge(('H', 'R'), add_reversed=False)
g.add_edge(('I', 'S'), add_reversed=False)
g.add_edge(('I', 'T'), add_reversed=False)
g.add_edge(('J', 'U'), add_reversed=False)
g.add_edge(('J', 'V'), add_reversed=False)

plus_inf = float('inf')
minus_inf = float('-inf')
values = {'A': minus_inf, 'B': plus_inf, 'C': plus_inf, 'D': plus_inf, 'E': minus_inf, 'F': minus_inf, 'G': minus_inf,
          'H': minus_inf, 'I': minus_inf, 'J': minus_inf, 'K': 4, 'L': 6, 'M': 7, 'N': 9, 'O': 1, 'P': 2, 'Q': 0,
          'R': 1, 'S': 8, 'T': 1, 'U': 9, 'V': 2}


def other_player(player):
    return 'MIN' if player == 'MAX' else 'MAX'


def minimax(graph, node, player):
    if not math.isinf(values[node]):
        return values[node]
    best = plus_inf if player == 'MIN' else minus_inf
    for child in graph[node]:
        result = minimax(graph, child, other_player(player))
        if player == 'MIN' and result < best:
            best = result
        elif player == 'MAX' and result > best:
            best = result
    return best


game_result = minimax(g.graph_dict, 'A', 'MAX')
print(game_result)
