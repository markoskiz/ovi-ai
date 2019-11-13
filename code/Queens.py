import os
from collections import deque
import numpy as np
from matplotlib import pyplot as plt
import skimage
from skimage import io

image_directory = 'queen images'
N = 15


def is_valid(new_state, new_queen_i, new_queen_j):
    vertical_check = new_queen_j not in new_state
    if not vertical_check:
        return False
    main_diagonal = new_queen_i - new_queen_j
    anti_diagonal = new_queen_i + new_queen_j
    other_queens = new_state[:N - new_state.count(None)]
    for other_queen_i, other_queen_j in enumerate(other_queens):
        if other_queen_i - other_queen_j == main_diagonal:
            return False
        if other_queen_i + other_queen_j == anti_diagonal:
            return False
    return True


def expand_state(state):
    new_states = []
    available_places = state.count(None)
    if not available_places:
        return []
    new_queen_i = N - available_places
    for new_queen_j in range(N):
        if is_valid(state, new_queen_i, new_queen_j):
            new_state = list(state)
            new_state[new_queen_i] = new_queen_j
            new_states.append(tuple(new_state))
    return new_states


def search(initial_state):
    visited = {initial_state}
    states_queue = deque([initial_state])
    while states_queue:
        state_to_expand = states_queue.popleft()
        for next_state in expand_state(state_to_expand):
            if next_state not in visited:
                if next_state.count(None) == 0:
                    return next_state
                visited.add(next_state)
                states_queue.appendleft(next_state)
    return


def visualise_queens(queens):
    if not queens:
        print('Не постои решение за N =', N)
        return
    border_color = (0, 0, 0, 1)
    queen = skimage.img_as_float(io.imread('queen.png'))
    table = np.zeros((queen.shape[0] * N, queen.shape[1] * N, queen.shape[2]))
    margin = queen.shape[0] // 20
    for i, j in enumerate(queens):
        table[i*queen.shape[0]:(i+1)*queen.shape[0], j*queen.shape[1]:(j+1)*queen.shape[1]] = queen
    for index in range(1, N):
        table[index * queen.shape[0] - margin: index * queen.shape[0] + margin] = border_color
        table[:, index * queen.shape[1] - margin: index * queen.shape[1] + margin] = border_color
    plt.imsave('{}/{}.png'.format(image_directory, N), table)
    plt.imshow(table)
    plt.title('Queen problem solution N = {}'.format(N))
    plt.show()


def main():
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    initial_state = (None,) * N
    queens = search(initial_state)
    visualise_queens(queens)


main()
