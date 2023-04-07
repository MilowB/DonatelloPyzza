'''
Author: Alexandru Valeanu
Adapted by: Mickael Bettinelli - 2023
'''

from numpy.random import random_integers as rand
import os, sys, inspect

#Pour inclure les fichiers de l'environnement
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

from draw_maze import ascii_representation

from constants import *


class Maze:
    def __init__(self, rows, columns):
        assert rows >= 1 and columns >= 1

        self.nrows = rows
        self.ncolumns = columns
        self.board = np.zeros((rows, columns), dtype=WALL_TYPE)
        self.board.fill(EMPTY)

    def set_borders(self):
        self.board[0, :] = self.board[-1, :] = WALL
        self.board[:, 0] = self.board[:, -1] = WALL

    def is_wall(self, x, y):
        assert self.in_maze(x, y)
        return self.board[x][y] == WALL

    def is_turtle(self, x, y):
        assert self.in_maze(x, y)
        return self.board[x][y] == TURTLE

    def is_pizza(self, x, y):
        assert self.in_maze(x, y)
        return self.board[x][y] == PIZZA

    def set_wall(self, x, y):
        assert self.in_maze(x, y)
        self.board[x][y] = WALL

    def set_turtle_position(self, x, y):
        self.board[x][y] = TURTLE

    def set_pizza_position(self, x, y):
        self.board[x][y] = PIZZA

    def remove_wall(self, x, y):
        assert self.in_maze(x, y)
        self.board[x][y] = EMPTY

    def in_maze(self, x, y):
        return 0 <= x < self.nrows and 0 <= y < self.ncolumns

    def write_to_file(self, filename):
        f = open(filename, 'w')
        f.write(ascii_representation(self))
        f.close()

    @staticmethod
    def create_maze(rows, columns, seed=None, complexity=.5, density=.2):
        startPosition = 1
        pizzaPosition = 1

        rows = (rows // 2) * 2 + 1
        columns = (columns // 2) * 2 + 1

        if seed is not None:
            np.random.seed(seed)

        # Adjust complexity and density relative to maze size
        complexity = int(complexity * (5 * (rows + columns)))
        density = int(density * ((rows // 2) * (columns // 2)))

        maze = Maze(rows, columns)
        maze.set_borders()

        # Make aisles
        for i in range(density):
            x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
            maze.set_wall(x, y)

            for j in range(complexity):
                neighbours = []

                if maze.in_maze(x - 2, y):
                    neighbours.append((x - 2, y))

                if maze.in_maze(x + 2, y):
                    neighbours.append((x + 2, y))

                if maze.in_maze(x, y - 2):
                    neighbours.append((x, y - 2))

                if maze.in_maze(x, y + 2):
                    neighbours.append((x, y + 2))

                if len(neighbours):
                    next_x, next_y = neighbours[rand(0, len(neighbours) - 1)]

                    if not maze.is_wall(next_x, next_y):
                        maze.set_wall(next_x, next_y)
                        maze.set_wall(next_x + (x - next_x) // 2, next_y + (y - next_y) // 2)
                        x, y = next_x, next_y

        x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
        while ((x+1 >= columns or x+1 >= rows or
            x-1 <= 0 or x-1 <= 0 or
            y+1 >= columns or y+1 >= rows or
            y-1 <= 0 or y-1 <= 0) or
            (maze.is_wall(x+1, y) and maze.is_wall(x-1, y) and maze.is_wall(x, y+1) and maze.is_wall(x, y-1))):
            x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
        tx, ty = x, y
        maze.set_turtle_position(x, y)

        x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
        while ((x+1 >= columns or x+1 >= rows or
            x-1 <= 0 or x-1 <= 0 or
            y+1 >= columns or y+1 >= rows or
            y-1 <= 0 or y-1 <= 0) or
            (maze.is_wall(x+1, y) and maze.is_wall(x-1, y) and maze.is_wall(x, y+1) and maze.is_wall(x, y-1)) or
            abs(tx-x) + abs(ty-y) <= (columns+rows)/4):
            x, y = rand(0, rows // 2) * 2, rand(0, columns // 2) * 2
        maze.set_pizza_position(x, y)

        return maze
