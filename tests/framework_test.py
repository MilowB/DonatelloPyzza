import os, sys, inspect
from envBuilder import *
import time
import random

'''
Actions
-------
0 - avancer
1 - toucher
2 - rotation gauche
3 - rotation droite
'''

def main():
    # Afficher ou non l'interface
    __ENVIRONMENT__ = "maze"
    __GUI__ = True

    # Instanciation des builders
    envbuilder = EnvBuilder(name=__ENVIRONMENT__, gui=__GUI__)
    # Creation de la grille
    turtle, env = envbuilder.build_grid()
    
    i = 0
    while i < 100:
        if i > 100 - 20:
            time.sleep(0.3)

        random_action = random.randint(0, 4)
        result = env.step(turtle, random_action)  # To use if the task is a  Maze
        print(result)


if __name__ == '__main__':
    main()