from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
from donatellopyzza import Assessor

from .game import *
from .mazeGenerator import MazeGenerator
from .assessor import Assessor
import random

class MySolution:
    # do not pass any parameter to this constructor
    def __init__(self):
        # save all the variables you need here
        self.lastAction = Action.MOVE_FORWARD

    # your solution needs to show this prototype to be used by the assessor
    # always call it "nextAction" and pass a single parameter which will be the feedback of your last action
    def nextAction(self, feedback):
        # process what you need to here
        nextAction = None
        if feedback == Feedback.TOUCHED_PIZZA:
            nextAction = self.lastAction
        else:
            if self.lastAction == Action.TOUCH:
                if feedback == Feedback.TOUCHED_WALL:
                    nextAction = Action.TURN_RIGHT
                elif feedback == Feedback.TOUCHED_NOTHING:
                    nextAction = Action.MOVE_FORWARD
            else:
                nextAction = Action.TOUCH
        self.lastAction = nextAction
        # return your action for this round
        return nextAction


if __name__ == '__main__':
    # create the assessor (nb runs, min height, min width, max height, max width)
    assessor = Assessor(100, 10, 10, 20, 20)
    # provide your solution
    assessor.setSolution(MySolution)
    # run the assessor and wait for your score
    assessor.run()