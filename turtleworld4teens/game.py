from turtle import Turtle
from envBuilder import *
import time
import random

class Game:
    def __init__(self, env, gui):
        self.env = env
        self.gui = gui
        pass

    def start(self):
        # Instanciate the envBuilder
        envbuilder = EnvBuilder(name=self.env, gui=self.gui)
        # creates the grid and the turtle
        agent, env = envbuilder.build_grid()
        return Turtle(agent, env)        