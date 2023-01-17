import os, sys, inspect

# Pour inclure les fichiers de l'environnement, plot et stat
cmd_subfolder_grid = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

from envBuilder import *
from grid import Grid
import time


def init_maze_task():

    __ENVIRONMENT__ = "maze"

    # Afficher ou non l'interface
    __GUI__ = True

    # Instanciation des builders
    envbuilder = EnvBuilder(__ENVIRONMENT__)
    gui, map, agents = envbuilder.build()

    # Creation de la grille
    env = Grid(gui, map, agents, __GUI__, __ENVIRONMENT__)

    return agents, env


'''
Actions
-------
0 - avancer
1 - toucher
2 - rotation gauche
3 - rotation droite
'''

def main():
    agents, env = init_maze_task()
    
    i = 0
    while i < 100:
        if i > 100 - 20:
            time.sleep(0.3)

        action = 1
        result = env.step(agents[0], action)  # To use if the task is a  Maze
        print(result)


if __name__ == '__main__':
    main()
