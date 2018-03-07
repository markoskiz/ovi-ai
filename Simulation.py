import os
from collections import deque
from time import sleep
import heapq
import numpy as np
from matplotlib import pyplot as plt

image_directory = 'search images'
world_shape = 20, 20
wall_notation = 0
path_color = (0.8, 0.5, 0.8)
agent_color = (0.8, 0, 0)
world_color = (1, 1, 0.8)
expanded_state_color = (0.5, 0.8, 0.5)
visited_state_color = (0.8, 1, 0.8)
goal_color = (0, 0, 0.8)
wall_color = (0, 0, 0)


class Simulation:
    def __init__(self, agent, goal, world, world_weight):
        plt.ion()
        self.figure = plt.figure()
        self.ax = plt.axes()
        self.ax.set_autoscaley_on(False)

        self.agent = agent
        self.goal = goal
        self.world = world
        self.world_weight = world_weight
        self.clean_world()

    def update_screen(self):
        plt.cla()
        self.ax.imshow(self.world)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def blind_search_visualised(self, search_algorithm):
        initial_state = self.agent
        states_queue = deque([[initial_state]])
        visited = {initial_state}
        while states_queue:
            states_list = states_queue.popleft()
            state_to_expand = states_list[-1]
            if state_to_expand != initial_state:
                self.world[state_to_expand] = expanded_state_color
            for next_state in self.expand_state(state_to_expand):
                if next_state not in visited:
                    visited.add(next_state)
                    if next_state == self.goal:
                        return states_list + [next_state]
                    if search_algorithm == 'breadth':
                        states_queue.append(states_list + [next_state])
                    elif search_algorithm == 'depth':
                        states_queue.appendleft(states_list + [next_state])
                    else:
                        raise AttributeError('{} is not a valid algorithm'.format(search_algorithm))
                    if all(self.world[next_state] != expanded_state_color):
                        self.world[next_state] = visited_state_color
            self.update_screen()
        return []

    def a_star_search_visualised(self, alpha, distance=None):
        """
        A* algorithm
        :param alpha: ratio between path cost and heuristic. weight = path_so_far + alpha * heuristic
        :param distance: heuristic function to use. Can be euclidean or manhattan
        :return: None
        """
        initial_state = self.agent
        expanded = set()
        states_queue = [((0, 0), [initial_state])]
        heapq.heapify(states_queue)
        while states_queue:
            current_weight, states_list = heapq.heappop(states_queue)
            current_a_star_weight, current_path_weight = current_weight
            state_to_expand = states_list[-1]
            if state_to_expand != initial_state:
                self.world[state_to_expand] = expanded_state_color
            if state_to_expand == self.goal:
                return states_list
            if state_to_expand in expanded:
                continue
            for next_state in self.expand_state(state_to_expand):
                transition_weight = self.world_weight[next_state] - self.world_weight[state_to_expand]
                step_cost = 0.01
                transition_weight = step_cost + max(transition_weight, 0)
                djikstra_weight = current_path_weight + transition_weight
                heuristic_weight = step_cost * self.distance(self.goal, next_state, distance) if distance else 0
                a_star_weight = (1 - alpha) * djikstra_weight + alpha * heuristic_weight
                if next_state not in expanded:
                    if all(self.world[next_state] != expanded_state_color):
                        self.world[next_state] = visited_state_color
                    heapq.heappush(states_queue, ((a_star_weight, djikstra_weight), states_list + [next_state]))
            expanded.add(state_to_expand)
            self.update_screen()
        return []

    def expand_state(self, state):
        agent_i, agent_j = state
        new_states = []
        if agent_i > 0:
            new_states.append((agent_i - 1, agent_j))
        if agent_j > 0:
            new_states.append((agent_i, agent_j - 1))
        if agent_i < world_shape[0] - 1:
            new_states.append((agent_i + 1, agent_j))
        if agent_j < world_shape[1] - 1:
            new_states.append((agent_i, agent_j + 1))
        new_states = [new_state for new_state in new_states if self.world_weight[new_state] != wall_notation]
        return new_states

    @staticmethod
    def distance(point_1, point_2, distance):
        if distance == 'manhattan':
            return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
        elif distance == 'euclidean':
            return np.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

    def clean_world(self):
        self.world[:] = world_color
        self.world[:, :, 0] = world_color[0] * self.world_weight
        self.world[:, :, 1] = world_color[1] * self.world_weight
        self.world[:, :, 2] = world_color[2] * self.world_weight
        self.world[self.agent] = agent_color
        self.world[self.goal] = goal_color

    def draw_path(self, path):
        self.world[self.agent] = agent_color
        for state in path[1:-1]:
            self.world[state] = path_color
        self.world[self.goal] = goal_color
        self.update_screen()
        sleep(2)

    def simulate_algorithm(self, algorithm, a_star_alpha=None, distance=None):
        self.clean_world()

        suptitle = {'depth': 'Depth first search', 'breadth': 'Breadth first search', 'djikstra': 'Djikstra search',
                    'greedy': 'Greedy search', 'a_star': 'A star'}
        if algorithm == 'a_star':
            filename = '{}/{}_{}_{:.3f}.png'.format(image_directory, algorithm, distance, a_star_alpha)
            plt.suptitle('{} {} {:.3f}'.format(suptitle[algorithm], distance, a_star_alpha))
        elif algorithm == 'greedy':
            filename = '{}/{}_{}.png'.format(image_directory, algorithm, distance)
            plt.suptitle('{} {}'.format(suptitle[algorithm], distance))
        else:
            filename = '{}/{}.png'.format(image_directory, algorithm)
            plt.suptitle(suptitle[algorithm])

        if algorithm in ['depth', 'breadth']:
            path = self.blind_search_visualised(algorithm)
        else:
            alpha = 0 if algorithm == 'djikstra' else 1 if algorithm == 'greedy' else a_star_alpha
            path = self.a_star_search_visualised(alpha, distance)

        self.draw_path(path)
        plt.imsave(filename, self.world)

    def simulate_all(self):
        self.simulate_algorithm('depth')
        self.simulate_algorithm('breadth')
        self.simulate_algorithm('djikstra')
        self.simulate_algorithm('greedy', distance='manhattan')
        self.simulate_algorithm('greedy', distance='euclidean')
        self.simulate_algorithm('a_star', a_star_alpha=0.5, distance='manhattan')
        self.simulate_algorithm('a_star', a_star_alpha=0.5, distance='euclidean')


def calc_cost(x, y):
    f = (x - 2 * world_shape[0] // 3) ** 2 + (y - world_shape[1] // 2) ** 2
    return f


def world_weight_playground():
    world_weight = np.array([calc_cost(x, y) for x in range(world_shape[0]) for y in range(world_shape[1])])
    world_weight = world_weight.reshape(world_shape)
    world_weight = 1 - world_weight / np.max(world_weight)
    world_weight[:4 * world_shape[0] // 5, world_shape[1] // 2] = wall_notation
    plt.suptitle('World weight')
    plt.imshow(world_weight)
    plt.colorbar()
    plt.show()
    return world_weight


def main():
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    agent = world_shape[0] // 2, world_shape[1] // 5
    goal = world_shape[0] // 5, 4 * world_shape[1] // 5
    world = np.zeros((world_shape[0], world_shape[1], 3), dtype=np.float)
    world_weight = world_weight_playground()
    world[world_weight == wall_notation] = wall_color
    sim = Simulation(agent, goal, world, world_weight)
    sim.simulate_all()


main()
