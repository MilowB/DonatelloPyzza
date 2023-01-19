from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
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
    
    # the hard-coded path to find the pizza in the maze environment
    actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
        Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
    
    # execute the path step by step
    for a in actions:
        time.sleep(0.5)
        result = turtle.execute(a)