from game import *
from action import *
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
    
    i = 0
    while i < 10:
        time.sleep(0.3)
        result = turtle.execute(Action.FORWARD)
        i += 1