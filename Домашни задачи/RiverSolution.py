import itertools
from collections import deque

passengers = ['Farmer', 'Goat', 'Cabbage', 'Wolf']
sailors = ['Farmer']


def other_side(side):
    return 'left' if side == 'right' else 'right'


def permited_river_bank(river_bank):
    if 'Goat' in river_bank and 'Wolf' in river_bank and 'Farmer' not in river_bank:
        return False
    if 'Cabbage' in river_bank and 'Goat' in river_bank and 'Farmer' not in river_bank:
        return False
    return True


def obtain_boat_trips(available_passengers):
    boat_trips = [(passenger,) for passenger in available_passengers if passenger in sailors]
    for possible_boat_trip in itertools.combinations(available_passengers, 2):
        sailors_on_boat = any([passenger in sailors for passenger in possible_boat_trip])
        if sailors_on_boat:
            boat_trips.append(possible_boat_trip)
    return boat_trips


def unpack_state(state):
    boat = state[0]
    left_bank = set([passengers[index] for index, side in enumerate(state[1:]) if side == 'left'])
    right_bank = set([passengers[index] for index, side in enumerate(state[1:]) if side == 'right'])
    return boat, left_bank, right_bank


def expand_state(state):
    boat, left_bank, right_bank = unpack_state(state)

    if boat == 'left':
        boat_trips = obtain_boat_trips(left_bank)
    else:
        boat_trips = obtain_boat_trips(right_bank)

    new_states = []
    for boat_trip in boat_trips:
        if boat == 'left':
            new_left_bank = left_bank - set(boat_trip)
            new_right_bank = right_bank | set(boat_trip)
        else:
            new_left_bank = left_bank | set(boat_trip)
            new_right_bank = right_bank - set(boat_trip)

        if permited_river_bank(new_left_bank) and permited_river_bank(new_right_bank):
            farmer = belongs('Farmer', new_left_bank, new_right_bank)
            goat = belongs('Goat', new_left_bank, new_right_bank)
            cabbage = belongs('Cabbage', new_left_bank, new_right_bank)
            wolf = belongs('Wolf', new_left_bank, new_right_bank)
            new_states.append((other_side(boat), farmer, goat, cabbage, wolf))

    return new_states


def search_path(initial_state, goal_state):
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
                states_queue.append(states_list + [next_state])
    return []


def separated_print(iterable):
    for element in iterable:
        print(element, end=' ')
    if not iterable:
        print('Empty', end='')


def visualise(path):
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


def belongs(passenger, left_side, right_side):
    if passenger in left_side:
        return 'left'
    elif passenger in right_side:
        return 'right'
    else:
        raise RuntimeError('Mayday, mayday, mayday. Passenger LOST')


def main():
    initial_state = ('left', 'left', 'left', 'left', 'left')
    goal_state = ('right', 'right', 'right', 'right', 'right')
    path = search_path(initial_state, goal_state)
    visualise(path)


main()
