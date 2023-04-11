from .turtleAgent import Turtle
from .envBuilder import *

import time
import random
from enum import Enum

class Action(Enum):
    MOVE_FORWARD = 0, "Move_forward"
    TURN_RIGHT = 1, "Turn_right"
    TURN_LEFT = 2, "Turn_left"
    TOUCH = 3, "Touch"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

    def __eq__(self, act):
        try:
            return self.value == act.value
        except:
            return False

# TODO: remove duplicate in grid.py
class Feedback(Enum):
    NO_FEEDBACK = -1, "No_feedback"
    COLLISION = 0, "Collision"
    MOVED = 1, "Moved"
    MOVED_ON_PIZZA = 2, "Moved_on_pizza"
    TOUCHED_WALL = 3, "Touched_wall"
    TOUCHED_NOTHING = 4, "Touched_nothing"
    TOUCHED_PIZZA = 5, "Touched_pizza"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

    def __eq__(self, fb):
        try:
            return self.value == fb.value
        except:
            return False

class Game:
    def __init__(self, envName, gui):
        self.envName = envName
        self.gui = gui
        self.env = None
        pass

    '''
    Goal : start the game by initializing the environment
    Return : a Turtle instance (a "user-friendly" wrapper class that includes one agent and the environment)
    '''
    def start(self):
        # Instanciate the envBuilder
        envbuilder = EnvBuilder(name=self.envName, gui=self.gui)
        # creates the grid and the turtle
        agent, env = envbuilder.build_grid()
        self.env = env
        return Turtle(agent, env)

    '''
    Goal : start the game by initializing the environment
    Return : True if the turtle found the pizza, else False
    '''
    def isWon(self, prnt=True):
        res = self.env.pizzaIsFound()
        if res and prnt:
            print("-----------------------------------------------------")
            print("###                  YOU WIN                      ###")
            print("-----------------------------------------------------")
            print("Pizza has been found with", self.env.nbActions, "actions !")
        return res

    def getScore(self):
        return self.env.nbActions
        



