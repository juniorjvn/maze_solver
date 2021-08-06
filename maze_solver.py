from maze_generator import create_maze, draw_maze
from random import randint
import time
import copy


def get_points(maze):
    total_blocks = len(maze)
    start = (0, 0)
    target = (0, 0)

    while maze[start[0]][start[1]]:
        start = (randint(0, total_blocks - 1), randint(0, total_blocks - 1))

    while maze[target[0]][target[1]]:
        target = (randint(0, total_blocks - 1), randint(0, total_blocks - 1))

    return start, target


def get_neighbors(pos, size):
    total_blocks = size * 2 + 1
    neighbors = []

    # check neighbor - UP
    x = pos[0] - 1
    if not x < 0:
        neighbors.append((x, pos[1]))

    # check neighbor - DOWN
    x = pos[0] + 1
    if not x > total_blocks - 1:
        neighbors.append((x, pos[1]))

    # check neighbor - LEFT
    y = pos[1] - 1
    if not y < 0:
        neighbors.append((pos[0], y))

    # check neighbor - RIGHT
    y = pos[1] + 1
    if not y > total_blocks - 1:
        neighbors.append((pos[0], y))

    return neighbors


def solve_maze(start, target, maze):
    temp_maze = copy.deepcopy(maze)
    length = len(temp_maze)
    path = {}
    explored = []
    frontier_queue = [start]

    while frontier_queue:
        current_cell = frontier_queue.pop(0)
        explored.append(current_cell)
        temp_maze[current_cell[0]][current_cell[1]] = 'o'

        time.sleep(0.5)
        print('\n\n')
        draw_maze(temp_maze)

        if current_cell == target:
            return path

        all_neighbors = get_neighbors(current_cell, length)
        neighbors = [neighbor for neighbor in all_neighbors
                     if neighbor not in explored and neighbor not in frontier_queue]

        for neighbor in neighbors:
            if not temp_maze[neighbor[0]][neighbor[1]]:
                path[neighbor] = current_cell
                frontier_queue.append(neighbor)


# SIZE = 7
# maze = create_maze((1, 1), SIZE)
# print(maze)
#
# start, target = get_points(maze)
# print('Start: {} - Target: {}'.format(start, target))
#
#
# draw_maze(maze)
#
# path = solve_maze(start, target, maze)

# i = target
# while i != start:
#     maze[i[0]][i[1]] = '.'
#     i = path[i]
#
# maze[start[0]][start[1]] = '.'
#
# draw_maze(maze)




'''
     Since our maze is surrounded by blocked by point, there is no need for special checking of
     invalid neighbors or out of bounds locations because nay point inside these border is guaranteed
     to have a UP, DOWN, LEFT, and RIGHT neighbor.
    '''


