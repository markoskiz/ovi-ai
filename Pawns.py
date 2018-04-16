import pawns_user_player as player1
import pawns_user_player as player2


class Board:
    def __init__(self, player_1, player_2, board_size=8, empty_slot='\u00B7'):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_sign = 'x'
        self.player_2_sign = 'o'
        self.board_size = board_size
        self.empty_slot = empty_slot
        self.board = [[empty_slot] * board_size] * board_size
        print((self.board[1][0]))
        self.board[0] = [self.player_1_sign] * board_size
        self.board[-1] = [self.player_2_sign] * board_size
        self.board[1][0] = 'x'
        print(type(self.board[1][0]))
        print((self.board[1][0]))
        print((self.board[2][0]))

    def draw_board(self):
        print(' ' * 2, end='')
        for index in range(self.board_size):
            print(' ', index, end='')
        print()
        for i, row in enumerate(self.board):
            print(i, '| ', end='')
            for j, element in enumerate(row):
                print(element, ' ' if j + 1 < len(row) else '', end='')
            print('|')
        print()

    def player_1_make_move(self, move):
        i, j, action = move
        print(i, j, action)
        self.board[i][j] = self.empty_slot
        if action == 'a':
            # self.board[i + 1][j] = self.player_1_sign
            self.board[i + 1][j] = 'q'
            print(self.board[i + 1][j])
        # elif action == 'l':
        #     self.board[i + 1][j + 1] = self.player_1_sign
        # elif action == 'r':
        #     self.board[i + 1][j - 1] = self.player_1_sign

    def player_2_make_move(self, move):
        i, j, action = move
        self.board[i][j] = self.empty_slot
        if action == 'a':
            self.board[i - 1][j] = self.player_2_sign
        elif action == 'l':
            self.board[i - 1][j - 1] = self.player_2_sign
        elif action == 'r':
            self.board[i - 1][j + 1] = self.player_2_sign

    def play(self):
        board.draw_board()
        while True:
            move = self.player_1.get_next_move()
            self.player_1_make_move(move)
            board.draw_board()
            if self.check_victory():
                print('Player 1 wins')
            print('check 1')
            move = self.player_2.get_next_move()
            self.player_2_make_move(move)
            board.draw_board()
            if self.check_victory():
                print('Player 2 wins')
            print('check 2')

    def check_victory(self):
        return True if self.player_2_sign in self.board[0] or self.player_1_sign in self.board[-1] else False


board = Board(player1, player2)
board.play()
