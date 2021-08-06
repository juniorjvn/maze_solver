from tkinter import *
from maze_solver import get_points, get_neighbors
from maze_generator import create_maze
import time
import copy

BLOCKS = 20
BLOCK_SIZE = 15
TOTAL_BLOCKS = BLOCKS * 2 + 1
SPEED = 0.001

WIDTH = BLOCK_SIZE * TOTAL_BLOCKS
HEIGHT = WIDTH


def draw_maze(win, canvas, maze):
    for i in range(TOTAL_BLOCKS):
        for j in range(TOTAL_BLOCKS):
            x = j * BLOCK_SIZE
            y = i * BLOCK_SIZE

            color = ""
            if maze[i][j]:
                color = 'black'
            else:
                color = 'white'

            canvas.create_rectangle(x, y, x+BLOCK_SIZE, y+BLOCK_SIZE, fill=color, outline=color)
    win.update()


def set_points(win, canvas, start, target):
    start_x = start[1] * BLOCK_SIZE
    start_y = start[0] * BLOCK_SIZE
    target_x = target[1] * BLOCK_SIZE
    target_y = target[0] * BLOCK_SIZE

    canvas.create_rectangle(start_x, start_y, start_x + BLOCK_SIZE, start_y + BLOCK_SIZE, fill='red', outline='')
    canvas.create_text(start_x + 7.5, start_y + 7.5, fill='white', font='Times 15 italic bold', text='S')
    canvas.create_rectangle(target_x, target_y, target_x + BLOCK_SIZE, target_y + BLOCK_SIZE, fill='green', outline='')
    canvas.create_text(target_x + 7.5, target_y + 7.5, fill='white', font='Times 15 italic bold', text='T')

    win.update()


def draw_path(win, canvas, path, start, target):
    block_path = path[target]
    done = (block_path == start)
    while not done:
        x = block_path[1] * BLOCK_SIZE
        y = block_path[0] * BLOCK_SIZE
        canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill='green', outline='')
        WIN.update()
        time.sleep(SPEED)

        block_path = path[block_path]
        done = (block_path == start)

    x = start[1] * BLOCK_SIZE
    y = start[0] * BLOCK_SIZE
    canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill='green', outline='')
    canvas.create_text(x + 7.5, y + 7.5, fill='white', font='Times 15 italic bold', text='S')
    win.update()


def search_path(win, canvas, maze, start, target):
    path = {}
    frontier_queue = [start]
    explored = []
    temp_maze = copy.deepcopy(maze)

    while frontier_queue:
        current_cell = frontier_queue.pop(0)
        explored.append(current_cell)
        temp_maze[current_cell[0]][current_cell[1]] = True

        x = current_cell[1] * BLOCK_SIZE
        y = current_cell[0] * BLOCK_SIZE
        canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill='red', outline='')
        WIN.update()
        time.sleep(SPEED)

        if current_cell == target:
            return path

        all_neighbors = get_neighbors(current_cell, BLOCKS)
        neighbors = [neighbor for neighbor in all_neighbors
                     if neighbor not in explored and neighbor not in frontier_queue]

        for neighbor in neighbors:
            if not temp_maze[neighbor[0]][neighbor[1]]:
                path[neighbor] = current_cell
                frontier_queue.append(neighbor)


start_time = time.perf_counter()
WIN = Tk()
canvas = Canvas(WIN, width=WIDTH, height=HEIGHT)
canvas.pack()

maze = create_maze((1,1), BLOCKS)
draw_maze(WIN, canvas, maze)

start, target = get_points(maze)
set_points(WIN, canvas, start, target)
time.sleep(7)

path = search_path(WIN, canvas, maze, start, target)

time.sleep(SPEED)
draw_maze(WIN, canvas, maze)
set_points(WIN, canvas, start, target)

draw_path(WIN, canvas, path, start, target)

end_time = time.perf_counter()
print('finish in', round(end_time - start_time, 2), 'second')

WIN.mainloop()


















