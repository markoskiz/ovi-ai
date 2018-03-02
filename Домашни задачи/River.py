from collections import deque

passengers = ['Farmer', 'Goat', 'Cabbage', 'Wolf']
sailors = ['Farmer']


def expand_state(state):
    """
    Function for generation next states.

    Your should return a list of states as tuples. List new_states should look like this:
    [(state_parameter_1, state_parameter_2, ... state_parameter_n),
    (state_parameter_1, state_parameter_2, ... state_parameter_n)),
    .
    .
    .
    (state_parameter_1, state_parameter_2, ... state_parameter_n))]

    :param state: state to be expanded
    :return: list of new states as tuples
    """
    # За полесни пресметки јас вака ги претставив објектите. Слободно променете ако имате подобра идеја.
    boat, left_bank, right_bank = unpack_state(state)

    new_states = []

    # Вашиот код тука

    return new_states


def unpack_state(state):
    """
    Function that carefully unpacks the state into boat, left side and right side
    :param state: state to be unpack
    :return: boat, left side objects, right side objects
    """
    boat = state[0]
    left_bank = set([passengers[index] for index, side in enumerate(state[1:]) if side == 'left'])
    right_bank = set([passengers[index] for index, side in enumerate(state[1:]) if side == 'right'])
    return boat, left_bank, right_bank


def search_path(initial_state, goal_state):
    """
    Search function
    :param initial_state: initial state for search
    :param goal_state: desired state
    :return: search result as list of states
    """
    visited = {initial_state}
    states_queue = deque([[initial_state]])
    while states_queue:
        states_list = states_queue.popleft()
        state_to_expand = states_list[-1]
        for next_state in expand_state(state_to_expand):
            if next_state not in visited:
                if next_state == goal_state:
                    return states_list + [next_state]
                visited.add(next_state)
                states_queue.appendleft(states_list + [next_state])
    return []


def separated_print(iterable):
    """
    Desired print function.
    :param iterable: list to be printed
    :return: None
    """
    for element in iterable:
        print(element, end=' ')
    if not iterable:
        print('Empty', end='')


def visualise(path):
    """
    Function to visualise path returned from the search function
    :param path: path to be visualised
    :return: None
    """
    if not path:
        print('Search path did not find a solution')
        return
    for pair_of_states in zip(path, path[1:]):
        boat_old, left_old, right_old = unpack_state(pair_of_states[0])
        boat_new, left_new, right_new = unpack_state(pair_of_states[1])
        delimiter_space = ' ' * 50
        separated_print(left_old)
        print(delimiter_space, end='')
        separated_print(right_old)
        print()
        if boat_old == 'left':
            delimiter = ' ' * 5 + '>' * 15 + ' ' * 5
            separated_print(left_new)
            print(delimiter, end='')
            separated_print(left_old - left_new)
            print(delimiter, end='')
            separated_print(right_old)
            print()
        else:
            delimiter = ' ' * 5 + '<' * 15 + ' ' * 5
            separated_print(left_old)
            print(delimiter, end='')
            separated_print(right_old - right_new)
            print(delimiter, end='')
            separated_print(right_new)
            print()
        separated_print(left_new)
        print(delimiter_space, end='')
        separated_print(right_new)
        print()
        print()
        print()


def main():
    # Јас вака ги означував состојбите. Слободно променете ако имате подобра идеја.
    initial_state = ('left', 'left', 'left', 'left', 'left')
    goal_state = ('right', 'right', 'right', 'right', 'right')
    path = search_path(initial_state, goal_state)
    visualise(path)


main()
