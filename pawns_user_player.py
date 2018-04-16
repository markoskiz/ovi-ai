BOARD_SIZE = 8
PAWN_ACTIONS = ['a', 'l', 'r']
EMPTY_SLOT = '\u00B7'


def read_user_input():
    message = input('Внесете потег: ').split()
    while True:
        try:
            i, j, action = int(message[0]), int(message[1]), message[2]
            if 0 <= i < BOARD_SIZE and 0 <= j < BOARD_SIZE and action in PAWN_ACTIONS:
                return i, j, action
            message = input('Лоша синтакса. pawn_i pawn_j pawn_action ').split()
        except IndexError:
            message = input('Лоша синтакса. pawn_i pawn_j pawn_action ').split()


def get_next_move():
    return read_user_input()
