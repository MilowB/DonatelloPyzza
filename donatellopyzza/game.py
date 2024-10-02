from turtleAgent import Turtle
from envBuilder import *

import time
import random
from enum import Enum

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
        turtle = Turtle(agent, env)
        # make the turtle touch before starting the game to get a position
        env.updatePosition(turtle.agent)
        return turtle

    '''
    Goal : get a dictionary of every non-wall squares with None values
    Return : return the aforementioned dictionary
    '''
    def getSquaresDict(self):
        return self.env.getSquaresAsDict()


    def updateSquareColor(self, key, color):
        self.env.updateSquareColor(key, color)
        
    def updateSquareText(self, key , text):
        self.env.updateSquareText(key, text)




    '''
    Goal : modify the color of each non-wall square
    Param : colors - a dictionary with keys (x, y) and pygame.Color as values
    '''
    def setSquaresColors(self, colors):
        self.env.setSquaresColors(colors)

    '''
    Goal : modify the text of each non-wall square
    Param : texts - a dictionary with keys (x, y) and string as values
    '''
    def setSquaresText(self, texts):
        self.env.setSquaresText(texts)

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
        



