from collections import deque
import numpy as np
from matplotlib import pyplot as plt
import heapq

world_shape = 20, 20
agent_color = (0.8, 0, 0)
world_color = (1, 1, 0.8)
expanded_state_color = (0.5, 0.8, 0.5)
visited_state_color = (0.8, 1, 0.8)
goal_color = (0, 0, 0.8)


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

    def update_screen(self, image):
        plt.cla()
        self.ax.imshow(image)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def blind_search_visualised(self, search_algorithm):
        initial_state = self.agent
        states_queue = deque([initial_state])
        visited = {initial_state}
        while states_queue:
            state_to_expand = states_queue.popleft()
            if state_to_expand != initial_state:
                self.world[state_to_expand] = expanded_state_color
            for next_state in self.expand_state(state_to_expand):
                if next_state not in visited:
                    visited.add(next_state)
                    if next_state == self.goal:
                        return
                    if search_algorithm == 'breadth':
                        states_queue.append(next_state)
                    elif search_algorithm == 'depth':
                        states_queue.appendleft(next_state)
                    else:
                        raise AttributeError('{} is not a valid algorithm'.format(search_algorithm))

                    if all(self.world[next_state] != expanded_state_color):
                        self.world[next_state] = visited_state_color
            self.update_screen(self.world)

    def a_star_search_visualised(self, alpha, distance='manhattan'):
        """
        A* algorithm
        :param alpha: ratio between path cost and heuristic. weight = path_so_far + alpha * heuristic
        :param distance: heuristic function to use. Can be euclidean or manhattan
        :return: None
        """
        initial_state = self.agent
        expanded = set()
        states_queue = [(0, initial_state)]
        heapq.heapify(states_queue)
        while states_queue:
            current_weight, state_to_expand = heapq.heappop(states_queue)
            if state_to_expand != initial_state:
                self.world[state_to_expand] = expanded_state_color
            if state_to_expand == self.goal:
                return
            if state_to_expand in expanded:
                continue
            for next_state in self.expand_state(state_to_expand):
                transition_weight = self.world_weight[next_state] - self.world_weight[state_to_expand]
                djikstra_weight = 0.01 + current_weight + transition_weight
                heuristic_weight = self.distance(self.goal, next_state, distance)
                a_star_weight = (1 - alpha) * djikstra_weight + alpha * heuristic_weight
                if next_state not in expanded:
                    if all(self.world[next_state] != expanded_state_color):
                        self.world[next_state] = visited_state_color
                    heapq.heappush(states_queue, (a_star_weight, next_state))
            expanded.add(state_to_expand)
            self.update_screen(self.world)

    @staticmethod
    def expand_state(state):
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

    def simulate(self):
        self.clean_world()
        plt.suptitle('Depth first search')
        self.blind_search_visualised('depth')
        plt.imsave('images/dfs.png', self.world)

        self.clean_world()
        plt.suptitle('Breadth first search')
        self.blind_search_visualised('breadth')
        plt.imsave('images/bfs.png', self.world)

        self.clean_world()
        plt.suptitle('Djikstra search')
        self.a_star_search_visualised(0)
        plt.imsave('images/djikstra.png', self.world)

        self.clean_world()
        plt.suptitle('Greedy search manhattan')
        self.a_star_search_visualised(1, 'manhattan')
        plt.imsave('images/greedy_manhattan.png', self.world)

        self.clean_world()
        plt.suptitle('Greedy search euclidean')
        self.a_star_search_visualised(1, 'euclidean')
        plt.imsave('images/greedy_euclidean.png', self.world)

        self.clean_world()
        plt.suptitle('A star search manhattan')
        self.a_star_search_visualised(0.8, 'manhattan')
        plt.imsave('images/a_star_manhattan.png', self.world)

        self.clean_world()
        plt.suptitle('A star search euclidean')
        self.a_star_search_visualised(0.2, 'euclidean')
        plt.imsave('images/a_star_euclidean.png', self.world)


def calc_cost(x, y):
    f = (x - 2 * world_shape[0] // 3) ** 2 + (y - world_shape[1] // 2) ** 2
    return f


def world_weight_playground():
    world_weight = np.array([calc_cost(x, y) for x in range(world_shape[0]) for y in range(world_shape[1])])
    world_weight = world_weight.reshape(world_shape)
    world_weight = 1 - world_weight / np.max(world_weight)
    plt.suptitle('World weight')
    plt.imshow(world_weight)
    plt.colorbar()
    plt.show()
    return world_weight


def main():
    agent = world_shape[0] // 2, 0
    goal = world_shape[0] - 1 - 1, world_shape[1] - 1 - 1
    world = np.zeros((world_shape[0], world_shape[1], 3), dtype=np.float)
    world_weight = world_weight_playground()
    sim = Simulation(agent, goal, world, world_weight)
    sim.simulate()


main()
