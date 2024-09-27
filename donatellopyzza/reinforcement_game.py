from donatellopyzza import RLGame
from donatellopyzza import Action
from donatellopyzza import Feedback

from random import randint
import pygame
import time

if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    rlgame = RLGame(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = rlgame.start()
    
    while not rlgame.isWon():
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
            Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
        # execute the path step by step
        for a in actions:
            position = rlgame.getTurtlePosition(turtle)
            orientation = rlgame.getTurtleOrientation(turtle)
            print("Turtle is on square", position, "and faces", orientation)
            result, _ = turtle.execute(a)
            time.sleep(1)