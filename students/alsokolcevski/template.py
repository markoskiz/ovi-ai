import itertools
from collections import deque


# ~~~~~~~~|=>  START  <=|~~~~~~~~ #

#  STEP 1: Make a list of all passengers and sailors
    # Passengers -> Every member in the story
passengers = ['goat', 'wolf', 'cabbage', 'farmer']

    # Sailors -> The members who can drive the boat 
    # (those who MUST be in the boat on any given trip)
sailors = ['farmer']

max_members = 2

    # STEP 2: Define the starting state and goal state
def main():

    # State - array of positions -> 0-left 1-right
    start_state = ('left',) * ( len(passengers) + 1 ) # First 0 is for the boat
    goal_state  = ('right',) * ( len(passengers) + 1 )
    path = search_path(start_state, goal_state)
    # print(path)
    visualise(path)



# STEP 3: Define the functions needed to solve this

#   STEP 3.1: Define the search_path function

# search_path is the search algorithm, with expand_state being 
# the function that generates the next states
def search_path(start, goal):

    if start == goal:
        print("You're already there...")
        return

    # We use the DEPTH FIRST SEARCH ALGORITHM because:
    #   - the expand_state function generates ONLY the valid states
    #   - this means we won't be lead astray by the greediness of DFS
    #   - on the contrary, we will benefit from its speed 
    #   because it will quickly go down the ONLY path we can take

    # DFS SEARCH ALGORITHM:
    visited = {start}   # A set of the states that have been visited
    queue = deque([[start]])    # The queue containing a list of all the paths

    while queue:

        path = queue.popleft()      # We take the FIRST path in the list of all paths (the queue)
        current_state = path[-1]    # We take the LAST state in the path we are examining

        for neighbour in expand_state(current_state):

            if neighbour not in visited:

                # Check for test case
                if neighbour == goal:
                    # We found the solution!
                    # print("Found solution! \n")
                    return path + [neighbour]
                
                # This code is basically the else case
                visited.add(neighbour)
                queue.appendleft(path + [neighbour]) # because we are using DFS
    return []


# STEP 3.2: Define the expand_state function

#   EXPAND STATE FUNCTION DOES 3 MAIN THINGS:

#       1. Gets the information about the current state -> using get_state()
#       2. Generates all possible boat trips from the current state -> using generate_boat_trips()
#       3. Generates new states
#           - using set operations to make the new river banks
#           - checks if those river banks are valid -> using check_state_calidity() 
def expand_state(state):

    # 1. Getting info about the current state
    boat, left_bank, right_bank = get_state(state)


    # 2. Generating boat trips
    if boat == 'left':
        boat_trips = generate_boat_trips(left_bank)
    else:
        boat_trips = generate_boat_trips(right_bank)


    new_states = []

    # 3. Generating new states
    for boat_trip in boat_trips:

        # 3.1 Set operations
        if boat == 'left':
            # Take away the members from the left side with the "-" set operator [RAZLIKA]
            new_left_bank = left_bank - set(boat_trip)
            # Add the members to the right side with the "|" set operator [UNIJA]
            new_right_bank = right_bank | set(boat_trip)
        else:
            # Take away the members from the right side
            new_right_bank = right_bank - set(boat_trip)
            # Add the members to the left side
            new_left_bank = left_bank | set(boat_trip)


        # 3.2 Check validity
        if check_state_validity(boat_trip, new_left_bank) and check_state_validity(boat_trip, new_right_bank):
            # If this state of the left and right bank is VALID:
                        

            # Vaka stefan go naprail:
            
            # This can be changed with a for loop
            # farmer = get_side('Farmer', new_left_bank, new_right_bank)
            # goat = get_side('Goat', new_left_bank, new_right_bank)
            # cabbage = get_side('Cabbage', new_left_bank, new_right_bank)
            # wolf = get_side('Wolf', new_left_bank, new_right_bank)
            # new_states.append((other_side(boat), farmer, goat, cabbage, wolf))


            # Vaka ke vazi za bilo koja zadaca:

            # We first make a new_state variable
            new_state = []
            # We add the OTHER SIDE of the boat -> simulating the boat crossing the river
            new_state.append(other_side(boat))
            
            # Then we traverse all passengers and check which side they are on
            for passenger in passengers:
                # We get the side that passenger is on with the get_side() function
                passenger_side = get_side(passenger, new_left_bank, new_right_bank)
                # And add it to the new state
                new_state.append(passenger_side)
            
            # Cast the new_state to a tuple, because out states ARE REPRESENTED AS TUPLES
            new_state = tuple(new_state)
            # Finally, add the new_state to the new_states list
            new_states.append(new_state)


    return new_states



# STEP 3.3: Define all the functions used in the expand_state() function


# The get_state() function sepparates the current state into information about:
#   - boat -> the state of the boat, 
#   - the left_bank -> state of the left bank 
#   - and right_bank -> the state of the right bank
def get_state(state):

    boat = state[0]

    left_bank = set()
    right_bank = set()

    for i in range(0, len(passengers)):

        if state[i+1] == 'left':
            # if member of state is on the left right bank
            left_bank.add(passengers[i])
        elif state[i+1] == 'right':
            # member is on the right bank
            right_bank.add(passengers[i])

    return boat, left_bank, right_bank


# The generate_boat_trips() function returns all possible boat trips we can take, given
# the passengers on the same side of the river that the boat is currently on
def generate_boat_trips(river_bank):

    boat_trips = []


    # First, we add all the possible trips that include ONLY the sailors in the boat
    for passenger in river_bank:
        if passenger in sailors:
            boat_trips.append((passenger,))

    # Then, we add all the other possible boat trips
    for possible_boat_trip in itertools.combinations(river_bank, max_members):
        # Vaka stefan go ima napraveno:
        # sailors_on_boat = any([passenger in sailors for passenger in possible_boat_trip])
        
        # Vaka jas go napraviv da mi bide pojasno sto se desava
        for sailor in sailors:
            if sailor in possible_boat_trip:
                # A sailor has to be in the boat for a boat trip to be deemed valid
                boat_trips.append(possible_boat_trip)
    

    return boat_trips



# The check_state_valivity() function is where we insert the conditions
# that apply to the ЗАДАЧА that we have :D
def check_state_validity(boat_trip, river_bank):

        # boat_trip parameter -> for conditions about the current boat trip 
        # river_bank parameter -> for conditions about the current river_bank

        # ******************* #
        # ~ CONDITIONS HERE ~ #
        if 'goat' in river_bank and 'cabbage' in river_bank and 'farmer' not in river_bank:
            return False
        if 'goat' in river_bank and 'wolf' in river_bank and 'farmer' not in river_bank:
            return False
        # ~ CONDITIONS HERE ~ #
        # ******************* #
                
        return True

    
# The other_side() function just returns the opposide side of the one the passenger(boat) is on
def other_side(boat_side):
    # The parameter is called boat_side, and not passenger_side because
    # we use this function only on the boat
    if boat_side == 'left':
        return 'right'
    return 'left'

    
# The get_side() function returns the side that the passenger is on, given
# the current left and right bank states
def get_side(passenger, left_bank, right_bank):

    if passenger in left_bank:
        return 'left'
    elif passenger in right_bank:
        return 'right'




# ************************ #

# DON'T NEED TO KNOW THIS  #
def separated_print(iterable):
    for element in iterable:
        print(element, end=' ')
    if not iterable:
        print('Empty', end='')

# DON'T NEED TO KNOW THIS  #
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

# ************************ #


# And thats it! :D

main()

# ~~~~~~~~|=>  END  <=|~~~~~~~~ #