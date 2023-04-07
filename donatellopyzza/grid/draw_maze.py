from matplotlib import pyplot
from matplotlib import colors
import pkg_resources
from pkg_resources import resource_string

import os, sys, inspect

#Pour inclure les fichiers de l'environnement
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)
    
import constants

def get_data_path(path, name):
    return pkg_resources.resource_filename(__name__, path + name)

def save_maze(maze, filename=None):
    pyplot.figure(figsize=(20, 10))

    path = get_data_path("../data/environments/", filename)
    color_path(maze, [])

    # make a color map of fixed colors
    cmap = colors.ListedColormap(['black', 'white', 'red', 'blue'])
    bounds = [0, 1, 2, 3, 4]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # tell imshow about color map so that only set colors are used
    pyplot.imshow(maze.board, interpolation='nearest',
                  cmap=cmap, norm=norm)

    pyplot.xticks([]), pyplot.yticks([])

    if path is not None:
        pyplot.savefig(path + ".png")
        maze.write_to_file(path + '.txt')


def ascii_representation(maze):
    rep = ''
    for i in range(maze.nrows):
        for j in range(maze.ncolumns):
            if maze.is_wall(i, j):
                rep += 'B'
            elif maze.is_turtle(i, j):
                rep += "a"
            elif maze.is_pizza(i, j):
                rep += "p"
            else:
                rep += ' '
        rep += '\n'
    return rep


def color_path(maze, path):
    for (x, y) in path:
        maze.board[x][y] = constants.RED

    if len(path):
        maze.board[path[0][0], path[0][1]] = constants.BLUE
        maze.board[path[-1][0], path[-1][1]] = constants.BLUE
