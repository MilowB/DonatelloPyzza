from .game import *
from .mazeGenerator import MazeGenerator
from .assessor import Assessor
import random

class Solution:
    def __init__(self):
        self.lastAction = Action.MOVE_FORWARD

    def nextAction(self, feedback):
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
        return nextAction


if __name__ == '__main__':
    # generation of the maze
    generator = MazeGenerator()
    maze = generator.create_maze(5, 5)
    filepath = "test"
    maze.save(maze, filename=filepath)

    # the name of the environment
    __ENVIRONMENT__ = "test"
    # display the interface (or not)
    __GUI__ = True


    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    sol = Solution()
    result = None
    while not game.isWon():
        time.sleep(0.3)
        r = random.randint(0, 3)
        action = sol.nextAction(result)
        result = turtle.execute(action)