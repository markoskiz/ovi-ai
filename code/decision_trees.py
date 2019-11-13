import numpy as np


def entropy_v1(q):
    if q == 0 or q == 1:
        return 0
    return -q * np.log2(q) - (1 - q) * np.log2(1 - q)


def entropy_v2(a, b):
    if a == 0 or b == 0:
        return 0
    m = a + b
    return - a / m * np.log2(a / m) - b / m * np.log2(b / m)


def best_choice(table):
    choice_entropy_list = []
    for feature_index in range(table.shape[1] - 1):
        table_1 = table[table[:, feature_index] == 1]
        table_0 = table[table[:, feature_index] == 0]
        choice_0_minus_count = len(table_0[:, -1][table_0[:, -1] == 0])
        choice_0_plus_count = len(table_0[:, -1][table_0[:, -1] == 1])
        choice_1_minus_count = len(table_1[:, -1][table_1[:, -1] == 0])
        choice_1_plus_count = len(table_1[:, -1][table_1[:, -1] == 1])
        choice_0_entropy = entropy_v2(choice_0_minus_count, choice_0_plus_count)
        choice_1_entropy = entropy_v2(choice_1_minus_count, choice_1_plus_count)
        choice_0_data_percentage = table_0.shape[0] / table.shape[0]
        choice_1_data_percentage = table_1.shape[0] / table.shape[0]
        choice_entropy = choice_0_entropy * choice_0_data_percentage + choice_1_entropy * choice_1_data_percentage
        choice_entropy_list.append(choice_entropy)

    lowest_entropy_choice = np.argmin(choice_entropy_list)
    return lowest_entropy_choice


def main():
    # f0, f1, f2, f3
    # Означувањето започнува од 0. Последната колона е излезот y.
    table = np.array([[0, 1, 1, 0, 0],
                      [1, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1],
                      [0, 0, 1, 1, 1],
                      [1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0]])
    lowest_entropy_choice = best_choice(table)
    print('Најдобро е да делиме по значајка f{}'.format(lowest_entropy_choice))


main()
