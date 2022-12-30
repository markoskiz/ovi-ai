from time import sleep
import random
from copy import deepcopy
import multiprocessing as mp
from plotly import graph_objects as go
import ipywidgets as ipw
from IPython import display


class Game:
    def __init__(self, state, player_1, player_2, time_to_play=10):
        self.N = len(state)
        self.time_to_play = time_to_play
        self.state_original = state
        self.state = deepcopy(self.state_original)
        self.player_1 = {**player_1, 'symbol': 'S'}
        self.player_2 = {**player_2, 'symbol': 'P'}
        self.next_to_play = self.player_1
        self.symbols_fig = {
            'S': 'star', 'P': 'pentagon', 'x': 'x', '·': 'circle-open'}
        self.scores = {'S': 1, 'P': -1}
        self.create_ui()
        hbox = ipw.HBox([self.bt_restart, self.dashboard])
        self.output = ipw.Output()
        vbox = ipw.VBox([hbox, self.fig, self.output])
        self.restart()
        display.display(vbox)

    def restart(self, *args):
        self.h_calls = 0
        self.max_depth = 0
        self.next_to_play = self.player_1
        self.next_human_move = 'queen_moves'
        self.update_score('На ред е', self.next_to_play)
        if self.next_to_play['type'] == 'human':
            self.dashboard.value += ' -- помести ја кралицата'
        self.state = deepcopy(self.state_original)
        self.evaluated = {}
        self.fig.data[0].marker.symbol = self.convert_state_to_symbols()
        self.winner = 'keep_playing'
        self.output.clear_output()

    def ck_bt_restart(self, bt_restart):
        self.restart()
        self.initiate_turn()

    def create_ui(self):
        self.dashboard = ipw.HTML(description='Статус:', value='')
        self.bt_restart = ipw.Button(description='Рестартирај')
        self.bt_restart.on_click(self.ck_bt_restart)
        self.fig = self.create_fig()

    def create_fig(self):
        fig = go.FigureWidget()
        x = [x for y in range(self.N) for x in range(self.N)]
        y = [y for y in range(self.N) for x in range(self.N)]
        symbols = [self.symbols_fig[v] for row in self.state for v in row]
        fig.add_scatter(x=x, y=y, mode='markers', marker_size=48,
                        marker_symbol=symbols, marker_color='LightSkyBlue',
                        marker_line_width=6, marker_line_color='MediumPurple')
        fig.data[0].on_click(self.human_move)
        fig.update_xaxes(
            range=[-0.5, self.N - 0.5], dtick=1, title='x', side='top')
        fig.update_yaxes(
            range=[-0.5, self.N - 0.5], dtick=1, title='y',
            autorange='reversed')
        fig.update_layout(width=600, height=600, showlegend=False)
        return fig

    def convert_state_to_symbols(self):
        return [self.symbols_fig[v] for row in self.state for v in row]

    def initiate_turn(self):
        if 'human' not in [self.player_1['type'], self.player_2['type']]:
            while self.winner == 'keep_playing':
                self.ai_move()
        elif self.next_to_play['type'] == 'AI':
            self.ai_move()

    def its_valid_response(self, move):
        if move == 'did not respond':
            return False, 'Player did not respond in time.'
        if move is None:
            return False, 'Player\'s response is None.'
        if type(move) not in [tuple, list]:
            return False, 'Player\'s response is not a tuple or a list.'
        if len(move) != 4:
            return False, 'Player\'s response is not a tuple of length 4.'
        mx, my, sx, sy = move
        if any([type(v) is not int for v in move]):
            return False, 'Player\'s response contains non-integer values.'
        if any([v < 0 or v >= self.N for v in move]):
            return False, 'Player\'s response contains out of range values.'
        mx, my, sx, sy = move
        state = deepcopy(self.state)
        qx, qy = self.find_queen(state, self.next_to_play['symbol'])
        valid_queens = list(self.possible_moves(state, qx, qy))
        if (mx, my) not in valid_queens:
            msg = f'Queen tries to move to an occupied place {(mx, my)}.'
            return False, msg
        state[my][mx] = state[qy][qx]
        state[qy][qx] = '·'
        valid_shots = list(self.possible_moves(state, mx, my))
        if (sx, sy) not in valid_shots:
            return False, f'Queen tries to shoot an occupied place {(sx, sy)}.'
        return True, ''

    def ai_move(self):
        self.dashboard.value += ' -- пресметува'
        name = self.next_to_play["name"]
        move = self.wait_for_player()
        qx, qy = self.find_queen(self.state, self.next_to_play['symbol'])
        valid, reason = self.its_valid_response(move)
        if valid:
            self.print_to_dash(f'{name} plays {move}.')
            mx, my, sx, sy = move
            self.state[my][mx] = self.state[qy][qx]
            self.state[qy][qx] = '·'
            self.update_after_state_change()
            self.state[sy][sx] = 'x'
        else:
            msg = f'{name} - Invalid move: {reason}'
            msg += ' A random move will be played.'
            self.print_to_dash(msg)
            valid_queens = list(self.possible_moves(self.state, qx, qy))
            mx, my = random.choice(valid_queens)
            self.state[my][mx] = self.state[qy][qx]
            self.state[qy][qx] = '·'
            self.update_after_state_change()
            valid_shots = list(self.possible_moves(self.state, mx, my))
            sx, sy = random.choice(valid_shots)
            self.state[sy][sx] = 'x'
        self.update_after_state_change()
        self.player_took_turn()

    def print_to_dash(self, msg):
        with self.output:
            display.display(msg)

    def wait_for_player(self):
        move = 'did not respond'
        players_script = self.next_to_play['script']
        queue = mp.Queue()
        args = (queue, deepcopy(self.state), self.next_to_play['symbol'])
        process = mp.Process(
            target=players_script.get_move_official, args=args)
        process.start()
        process.join(timeout=self.time_to_play)
        if process.is_alive():
            process.terminate()
        else:
            if not queue.empty():
                move = queue.get()
        queue.close()
        return move

    def human_move(self, trace, points, selector):
        x, y = points.xs[0], points.ys[0]
        keep_playing = self.winner == 'keep_playing'
        human_on_turn = self.next_to_play['type'] == 'human'
        if keep_playing and human_on_turn:
            if self.next_human_move == 'queen_moves':
                qx, qy = self.find_queen(
                    self.state, self.next_to_play['symbol'])
                if (x, y) in list(self.possible_moves(self.state, qx, qy)):
                    self.state[y][x] = self.state[qy][qx]
                    self.state[qy][qx] = '·'
                    self.update_after_state_change()
                    self.next_human_move = 'queen_shoots'
                    self.dashboard.value += ' -- пукај'
            elif self.next_human_move == 'queen_shoots':
                qx, qy = self.find_queen(
                    self.state, self.next_to_play['symbol'])
                if (x, y) in list(self.possible_moves(self.state, qx, qy)):
                    self.state[y][x] = 'x'
                    self.update_after_state_change()
                    self.next_human_move = 'queen_moves'
                    self.player_took_turn()
                    if self.next_to_play['type'] == 'AI':
                        if self.winner == 'keep_playing':
                            self.ai_move()

    def update_after_state_change(self):
        self.fig.data[0].marker.symbol = self.convert_state_to_symbols()
        if self.next_to_play['type'] == 'AI':
            sleep(1)

    def flip_next_player(self):
        if self.next_to_play == self.player_2:
            return self.player_1
        return self.player_2

    def player_took_turn(self):
        self.next_to_play = self.flip_next_player()
        self.winner = self.check_victory(
            self.state, self.next_to_play['symbol'])
        if self.winner != 'keep_playing':
            next_to_play = self.flip_next_player()
            self.update_score('Победник е', next_to_play)
            return
        self.update_score('На ред е', self.next_to_play)
        if self.next_to_play['type'] == 'human':
            self.dashboard.value += ' -- помести ја кралицата'

    def update_score(self, message, player):
        player_data = ' - '.join([player['name'], player['symbol']])
        self.dashboard.value = f'{message} <b> {player_data} </b>.'

    def find_queen(self, state, queen_symbol):
        for y in range(self.N):
            for x in range(self.N):
                if state[y][x] == queen_symbol:
                    return x, y

    def possible_moves(self, state, x, y):
        deltas = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            while 0 <= nx < self.N and 0 <= ny < self.N:
                if state[ny][nx] == '·':
                    yield nx, ny
                else:
                    break
                nx += dx
                ny += dy

    def other_queen_symbol(self, queen_symbol):
        return 'P' if queen_symbol == 'S' else 'S'

    def check_victory(self, state, queen_to_move__symbol):
        queen_to_move__symbol
        qx, qy = self.find_queen(state, queen_to_move__symbol)
        if list(self.possible_moves(state, qx, qy)) == []:
            return self.other_queen_symbol(queen_to_move__symbol)
        return 'keep_playing'

