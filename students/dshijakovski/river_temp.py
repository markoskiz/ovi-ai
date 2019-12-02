import itertools
from collections import deque

passengers = []
sailors = []
max_members = 2

def main():

    start_state = ('left',) * ( len(passengers) + 1 )
    goal_state  = ('right',) * ( len(passengers) + 1 )
    path = search_path(start_state, goal_state)
    visualise(path)


def search_path(start, goal):

    if start == goal:
        print("You're already there...")
        return

    visited = {start}
    queue = deque([[start]])

    while queue:

        path = queue.popleft()
        current_state = path[-1]

        for neighbour in expand_state(current_state):
            if neighbour not in visited:
                if neighbour == goal:
                    return path + [neighbour]
                
                visited.add(neighbour)
                queue.append(path + [neighbour])
    return []


def expand_state(state):

    boat, left_bank, right_bank = get_state(state)

    if boat == 'left':
        boat_trips = generate_boat_trips(left_bank)
    else:
        boat_trips = generate_boat_trips(right_bank)

    new_states = []

    for boat_trip in boat_trips:

        if boat == 'left':
            new_left_bank = left_bank - set(boat_trip)
            new_right_bank = right_bank | set(boat_trip)
        else:
            new_right_bank = right_bank - set(boat_trip)
            new_left_bank = left_bank | set(boat_trip)

        if check_state_validity(boat_trip, new_left_bank) and check_state_validity(boat_trip, new_right_bank):
            new_state = []
            new_state.append(other_side(boat))
            
            for passenger in passengers:
                passenger_side = get_side(passenger, new_left_bank, new_right_bank)
                new_state.append(passenger_side)
            
            new_state = tuple(new_state)
            new_states.append(new_state)

    return new_states


def get_state(state):
    boat = state[0]

    left_bank = set()
    right_bank = set()

    for i in range(0, len(passengers)):
        if state[i+1] == 'left':
            left_bank.add(passengers[i])
        elif state[i+1] == 'right':
            right_bank.add(passengers[i])

    return boat, left_bank, right_bank


def generate_boat_trips(river_bank):

    boat_trips = []

    for passenger in river_bank:
        if passenger in sailors:
            boat_trips.append((passenger,))

    for possible_boat_trip in itertools.combinations(river_bank, max_members):
        
        for sailor in sailors:
            if sailor in possible_boat_trip:
                boat_trips.append(possible_boat_trip)
    
    return boat_trips


def check_state_validity(boat_trip, river_bank):

        # ~ CONDITIONS HERE ~ #
        # ------------------- #
        # ~ CONDITIONS HERE ~ #
                
        return True

    
def other_side(boat_side):
    if boat_side == 'left':
        return 'right'
    return 'left'

    
def get_side(passenger, left_bank, right_bank):

    if passenger in left_bank:
        return 'left'
    elif passenger in right_bank:
        return 'right'



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
        boat_old, left_old, right_old = get_state(pair_of_states[0])
        boat_new, left_new, right_new = get_state(pair_of_states[1])
        delimiter_space = ' ' * 50
        separated_print(left_old)
        print(delimiter_space, end='')
        separated_print(right_old)
        print()
        print()
        if boat_old == 'left':
            delimiter = ' ' * 5 + '>' * 15 + ' ' * 5
            separated_print(left_new)
            print(delimiter, end='')
            separated_print(left_old - left_new)
            print(delimiter, end='')
            separated_print(right_old)
            print()
            print()
        else:
            delimiter = ' ' * 5 + '<' * 15 + ' ' * 5
            separated_print(left_old)
            print(delimiter, end='')
            separated_print(right_old - right_new)
            print(delimiter, end='')
            separated_print(right_new)
            print()
            print()
        separated_print(left_new)
        print(delimiter_space, end='')
        separated_print(right_new)
        print()
        print()
        print()
        print()


main()
