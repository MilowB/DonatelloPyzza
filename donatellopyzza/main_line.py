from .game import *
import random

if __name__ == '__main__':
    # load the new maze
    __ENVIRONMENT__ = "line"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()

    while not game.isWon():
        time.sleep(0.3)
        result = turtle.execute(Action.MOVE_FORWARD)