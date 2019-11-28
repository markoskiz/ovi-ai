from graph import Graph


plus_inf = float('inf')
minus_inf = float('-inf')

# Го правиме дрвото на играта.
g = Graph()
# Ги додаваме јазлите.
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
g.add_vertex('K')
g.add_vertex('L')
g.add_vertex('M')
g.add_vertex('N')
g.add_vertex('O')
g.add_vertex('P')
g.add_vertex('Q')
g.add_vertex('R')
g.add_vertex('S')
g.add_vertex('T')
g.add_vertex('U')
g.add_vertex('V')
# Ги додаваме врските помеѓу јазлите.
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
# Секој лист има вредност која го означува крајниот резултат на играта, 
# или пак евалуација на тој јазол ако немаме време да го разграниме целото дрво.
leafs = {'K': 4, 'L': 6, 'M': 7, 'N': 9, 'O': 1, 'P': 2, 'Q': 0, 'R': 1, 'S': 8, 'T': 1, 'U': 9, 'V': 2}


def other_player(player):
    """
    Оваа функција го враќа другиот играч кој е следен на потег.
    """
    return 'MIN' if player == 'MAX' else 'MAX'


def minimax(graph, node, player):
    """
    Оваа функција го имплементира минимакс алгоритамот. Ова е рекурзивна функција.
    :graph: Ова е дрвото за кое треба да разгрануваме
    :node: е коренот на дрвото
    :player: е играчот следен на потег, MIN или MAX
    """
#     Ако стигнеме да разгрануваме лист, тогаш ја враќаме вредноста на тој лист. 
#     Ова е резултат на играта или пак евалуација на моменталната состојба.
    if node in leafs:
        return leafs[node]
#     Во спортивно, треба да ја пресметаме вредноста на играта за тој јазол преку истражување на сите негови деца.
#     Ако сега на ред е MAX играчот тогаш моментално најдобриот избор за него е -inf.
#     Ако сега на ред е MIN играчот тогаш моментално најдобриот избор за него е inf.
    best = plus_inf if player == 'MIN' else minus_inf
#     Итерираме низ децата на коренот `node` за да го најдеме најдобриот потег за моменталниот играч `player`.
    for child in graph[node]:
#         За секое дете го пресметуваме резултатот на играта од детето па надолу низ сите негови гранки.
        result = minimax(graph, child, other_player(player))
#         Ако на ред е MIN играчот, тогаш за него ја бараме најмалата вредност за играта која ќе ја добиеме од неговите деца.
        if player == 'MIN' and result < best:
            best = result
#         Инаку, ако на ред е MAX играчот, тогаш за него ја бараме најголема вредност за играта која ќе ја добиеме од неговите деца.
        elif player == 'MAX' and result > best:
            best = result
    return best


def minimax_alpha_beta(graph, node, player, alpha=minus_inf, beta=plus_inf):
    """
    Оваа функција го имплементира минимакс алгоритамот заедно со алфа-бета поткаструвањето. Ова е рекурзивна функција.
    :graph: Ова е дрвото за кое треба да разгрануваме
    :node: е коренот на дрвото
    :player: е играчот следен на потег, MIN или MAX
    :alpha: е најдобриот потег за MAX играчот од јазолот кој е на ред за разгранување до коренот
    :beta: е најдобриот потег за MIN играчот од јазолот кој е на ред за разгранување до коренот
    """
#     Ако стигнеме да разгрануваме лист, тогаш ја враќаме вредноста на тој лист. 
#     Ова е резултат на играта или пак евалуација на моменталната состојба.
    if node in leafs:
        return leafs[node]
#     Во спортивно, треба да ја пресметаме вредноста на играта за тој јазол преку истражување на сите негови деца.
#     Ако сега на ред е MAX играчот тогаш моментално најдобриот избор за него е -inf.
#     Ако сега на ред е MIN играчот тогаш моментално најдобриот избор за него е inf.
    best = plus_inf if player == 'MIN' else minus_inf
#     Итерираме низ децата на коренот `node` за да го најдеме најдобриот потег за моменталниот играч `player`.
    for child in graph[node]:
#         За секое дете го пресметуваме резултатот на играта од детето па надолу низ сите негови гранки.
        result = minimax_alpha_beta(graph, child, other_player(player), alpha, beta)
#         Ако на ред е MIN играчот,
        if player == 'MIN':
#             Најпрво испитуваме дали најновата вредност за играта добиена од моменталното дете 
#             е помала или еднаква на alpha - моментално најдобрата вредност за MAX играчот од тука до коренот на дрвото.
#             Ако овој услов е исполнет, тогаш нема потреба да разгрануваме повеќе бидејќи колку и да е помала вредноста на играта.
#             која ќе ја пронајдеме од некое друго дете, MAX играчот ќе ја избере вредноста alpha еден степен погоре.
            if result <= alpha:
                return result
#             Во овој момент ја обновуваме вредноста на beta за да ја пратиме како аргумент на наредното дете 
#             како досега најдобра вредност за MIN играчот.
            if result < beta:
                beta = result
#             Ја бараме најмалата вредност на играта, бидејќи сега на ред е MIN, и ќе ја зачуваме како резултат во моменталниот јазол `node`.
            if result < best:
                best = result
#         Инаку, ако на ред е MAX играчот,
        elif player == 'MAX':
#             Најпрво испитуваме дали најновата вредност за играта добиена од моменталното дете 
#             е поголема или еднаква на beta - моментално најдобрата вредност за MIN играчот од тука до коренот на дрвото.
#             Ако овој услов е исполнет, тогаш нема потреба да разгрануваме повеќе бидејќи колку и да е поголема вредноста на играта
#             која ќе ја пронајдеме од некое друго дете, MIN играчот ќе ја избере вредноста beta еден степен погоре.
            if result >= beta:
                return result
#             Во овој момент ја обновуваме вредноста на alpha за да ја пратиме како аргумент на наредното дете 
#             како досега најдобра вредност за MAX играчот.
            if result > alpha:
                alpha = result
#             Ја бараме најголемата вредност на играта, бидејќи сега на ред е MAX, и ќе ја зачуваме како резултат во моменталниот јазол `node`.
            if result > best:
                best = result
    return best


game_result = minimax(g.graph_dict, 'A', 'MAX')
print(game_result)
game_result = minimax_alpha_beta(g.graph_dict, 'A', 'MAX')
print(game_result)
