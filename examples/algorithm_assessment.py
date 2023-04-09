from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
from donatellopyzza import Assessor

class MySolution:
    # do not pass any parameter to this constructor
    def __init__(self):
        # save all the variables you need here
        self.lastAction = Action.MOVE_FORWARD

    # your solution needs to show this prototype to be used by the assessor
    # always call it "nextAction" and add a single parameter which will be the feedback of your last action
    def nextAction(self, feedback):
        # process what you need to here
        nextAction = None
        if feedback == Feedback.TOUCHED_PIZZA:
            nextAction = Action.MOVE_FORWARD
        else:
            if self.lastAction == Action.MOVE_FORWARD:
                nextAction = Action.TURN_RIGHT
            elif self.lastAction == Action.TURN_RIGHT:
                nextAction = Action.TOUCH
            elif self.lastAction == Action.TOUCH and feedback == Feedback.TOUCHED_NOTHING:
                nextAction = Action.MOVE_FORWARD
            elif self.lastAction == Action.TOUCH and feedback == Feedback.TOUCHED_WALL:
                nextAction = Action.TURN_LEFT
            elif self.lastAction == Action.TURN_LEFT:
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