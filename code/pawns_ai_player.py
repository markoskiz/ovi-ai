from time import sleep
import random

BOARD_SIZE = 4
PAWN_ACTIONS = ['a', 'l', 'r']
EMPTY_SQUARE = '\u00B7'


def check_victory(board):
    return True if 'o' in board[0] or 'x' in board[-1] else False


def find_possible_moves(board, sign):
    sign_locations = [(i, j) for i, row in enumerate(board) for j, square in enumerate(row) if board[i][j] == sign]
    possible_moves = []
    if sign == 'x':
        for sign_i, sign_j in sign_locations:
            if board[sign_i + 1][sign_j] == EMPTY_SQUARE:
                possible_moves.append((sign_i, sign_j, 'a'))
            if sign_j > 0 and board[sign_i + 1][sign_j - 1] == 'o':
                possible_moves.append((sign_i, sign_j, 'r'))
            if sign_j < BOARD_SIZE - 1 and board[sign_i + 1][sign_j + 1] == 'o':
                possible_moves.append((sign_i, sign_j, 'l'))
    elif sign == 'o':
        for sign_i, sign_j in sign_locations:
            if board[sign_i - 1][sign_j] == EMPTY_SQUARE:
                possible_moves.append((sign_i, sign_j, 'a'))
            if sign_j > 0 and board[sign_i - 1][sign_j - 1] == 'x':
                possible_moves.append((sign_i, sign_j, 'l'))
            if sign_j < BOARD_SIZE - 1 and board[sign_i - 1][sign_j + 1] == 'x':
                possible_moves.append((sign_i, sign_j, 'r'))
    return possible_moves


def make_move(board, move, sign):
    i, j, action = move
    board[i][j] = EMPTY_SQUARE
    if sign == 'x':
        if action == 'a':
            board[i + 1][j] = 'x'
        elif action == 'l':
            board[i + 1][j + 1] = 'x'
        elif action == 'r':
            board[i + 1][j - 1] = 'x'
    elif sign == 'o':
        if action == 'a':
            board[i - 1][j] = 'o'
        elif action == 'l':
            board[i - 1][j - 1] = 'o'
        elif action == 'r':
            board[i - 1][j + 1] = 'o'


def next_move(board, my_sign, opponent_sign):
    """
    Тука треба да го вратите следниот потег кој би го одиграле.
    Потег се состои од (локација i на пиунот кој го поместувате, цел број во опсег [0..BOARD_SIZE),
                        локација j на пиунот кој го поместувате, цел број во опсег [0..BOARD_SIZE),
                        тип на поместување - може да биде:
                            'a' - оди напред
                            'l' - преземи пиун лево од тебе
                            'r' - преземи пиун десно од тебе
    На влез добивата табла како листа од листи. Секогаш Играч 1 е 'x', а Играч 2 е 'o'.
    Внимавајте на перспективата: Играч 1 'x' секогаш почнува од горе и напаѓа надолу.
                                 Играч 2 'x' секогаш почнува од доле и напаѓа нагоре.
    Бидејќи скриптата која ја пишувате може некогаш да биде Играч 1, а некогаш Играч 2, ја гледате променливата my_sign
    за да знаете со кој знак играте вие.

    Ваша задача е да имплементирате минимакс алгоритам кој ќе оцени кој потег е најдобро да се изигра од сите можни
    потези.
    :param board:
    :param my_sign:
    :param opponent_sign:
    :return:
    """
    possible_moves = find_possible_moves(board, my_sign)
    if possible_moves:
        move = possible_moves[random.randint(0, len(possible_moves) - 1)]
    return move
