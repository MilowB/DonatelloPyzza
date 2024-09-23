from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
import time

'''
# In this strategy, your turtle follow the wall at its right until it finds the pizza
'''
def strategy(previousAction, feedback):
    nextAction = None
    # if the pizza has been touched, then walk on it
    if feedback == Feedback.TOUCHED_PIZZA:
        nextAction = Action.MOVE_FORWARD
    else:
        # otherwise, the turtle follows the wall on its right
        if previousAction == Action.MOVE_FORWARD:
            nextAction = Action.TURN_RIGHT
        elif previousAction == Action.TURN_RIGHT:
            nextAction = Action.TOUCH
        elif previousAction == Action.TOUCH and feedback == Feedback.TOUCHED_NOTHING:
            nextAction = Action.MOVE_FORWARD
        elif previousAction == Action.TOUCH and feedback == Feedback.TOUCHED_WALL:
            nextAction = Action.TURN_LEFT
        elif previousAction == Action.TURN_LEFT:
            nextAction = Action.TOUCH
    previousAction = nextAction
    return nextAction, previousAction

if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    feedback = None
    previousAction = Action.MOVE_FORWARD
    while not game.isWon():
        time.sleep(0.3)
        nextAction, previousAction = strategy(previousAction, feedback)
        feedback, _ = turtle.execute(nextAction)