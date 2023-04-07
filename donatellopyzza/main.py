from .game import *
from .mazeGenerator import Maze
import random
import time


if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    while not game.isWon():
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
            Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
        # execute the path step by step
        for a in actions:
            time.sleep(0.3)
            result = turtle.execute(a)