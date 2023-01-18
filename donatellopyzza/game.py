from .turtleAgent import Turtle
from .envBuilder import *
# @DEBUG from .turtleAgent import Turtle
# @DEBUG ffrom .envBuilder import *
import time
import random

class Game:
    def __init__(self, envName, gui):
        self.envName = envName
        self.gui = gui
        pass

    def start(self):
        # Instanciate the envBuilder
        envbuilder = EnvBuilder(name=self.envName, gui=self.gui)
        # creates the grid and the turtle
        agent, env = envbuilder.build_grid()
        return Turtle(agent, env)


