import random
from copy import deepcopy

# задолжителена променлива, потполни ја со твои податоци
NAME = 'Име Презиме'


def find_queen(state, queen_symbol):
    N = len(state)
    for y in range(N):
        for x in range(N):
            if state[y][x] == queen_symbol:
                return x, y


def possible_moves(state, x, y):
    N = len(state)
    deltas = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if state[ny][nx] == '·':
                yield nx, ny
            else:
                break
            nx += dx
            ny += dy


def expand_state(state, symbol):
    qx, qy = find_queen(state, symbol)
    for mx, my in possible_moves(state, qx, qy):
        state_after_move = list([list(row) for row in state])
        state_after_move[my][mx] = symbol
        state_after_move[qy][qx] = '·'
        for sx, sy in possible_moves(state_after_move, mx, my):
            state_after_shot = deepcopy(state_after_move)
            state_after_shot[sy][sx] = 'x'
            state_after_shot = tuple([tuple(row) for row in state_after_shot])
            yield state_after_shot, (mx, my, sx, sy)


def other_queen_symbol(queen_symbol):
    return 'P' if queen_symbol == 'S' else 'S'


def check_victory(state, queen_to_move__symbol):
    queen_to_move__symbol
    qx, qy = find_queen(state, queen_to_move__symbol)
    if list(possible_moves(state, qx, qy)) == []:
        return other_queen_symbol(queen_to_move__symbol)
    return 'keep_playing'


def get_move_official(queue, state, symbol):
    """ Ова е официјалната функција која ќе биде повикана.

        НЕ МЕНУВАЈ НИШТО ВО ОВАА ФУНКЦИЈА.

        queue: multiprocessing.Queue
            Редица за да може да се проследи потегот до главниот процес.
        state: string
            Ова е моменталната состојба на таблата.
        symbol: str, {'S', 'P'}
            Ова е симболот на кралицата со која вие играте.

        Оваа функцијата не враќа податоци. Резултатот на играта треба да
        се запише во редицата `queue`. Структурата на одговорот е
        торка од две торки, една за новата позиција на кралицата,
        а другата за испуканото поле.
                        ((mx, my), (sx, sy))
        mx, my: се позициите на новата позиција на кралицата
        sx, sy: се позициите на испуканото поле

    """
    move = get_move(state, symbol)
    queue.put(move)


def get_move(state, symbol):
    other_symbol = 'S' if symbol == 'P' else 'P'
    minimax.scores = {symbol: 1, other_symbol: -1}
    result, move = minimax(state, 'MAX', symbol)
    return move


def minimax(state, player, symbol, alpha=-2, beta=2, depth=0):
    winner = check_victory(state, symbol)
    if winner != 'keep_playing':
        return minimax.scores[winner], None
    # пример како да се прекине со пребарување после длабочина 3
    if depth == 3:
        return evaluate_state(state, symbol), None
    best_value = 2 if player == 'MIN' else -2
    best_move = None
    for child, move in expand_state(state, symbol):
        other_player = 'MIN' if player == 'MAX' else 'MAX'
        other_symbol = 'S' if symbol == 'P' else 'P'
        result, _ = minimax(
            child, other_player, other_symbol, alpha, beta, depth+1)
        if player == 'MIN':
            if result <= alpha:
                return result, best_move
            if result < beta:
                beta = result
            if result < best_value:
                best_value = result
                best_move = move
        elif player == 'MAX':
            if result >= beta:
                return result, best_move
            if result > alpha:
                alpha = result
            if result > best_value:
                best_value = result
                best_move = move
    return best_value, best_move


def evaluate_state(state, symbol):
    # Ова е функцијата за проценката на победникот
    return 2 * random.random() - 1  # случаен број од -1 до 1
