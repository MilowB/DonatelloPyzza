from donatellopyzza import MazeGenerator
from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
from donatellopyzza import Assessor
import random
import unittest

class ExampleTests(unittest.TestCase):

    def test_basic_example(self):
        # the name of the environment
        __ENVIRONMENT__ = "maze"
        # display the interface (or not)
        __GUI__ = False

        game = Game(__ENVIRONMENT__, __GUI__)
        # returns a turtle that execute actions on its environment
        turtle = game.start()
        
        while not game.isWon():
            actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
                Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
            # execute the path step by step
            for a in actions:
                result = turtle.execute(a)
        self.assertEqual(game.getScore(), 6)

    def test_basic_strategy(self):
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

        # the name of the environment
        __ENVIRONMENT__ = "maze"
        # display the interface (or not)
        __GUI__ = False

        game = Game(__ENVIRONMENT__, __GUI__)
        # returns a turtle that execute actions on its environment
        turtle = game.start()
        
        feedback = None
        previousAction = Action.MOVE_FORWARD
        while not game.isWon():
            nextAction, previousAction = strategy(previousAction, feedback)
            feedback = turtle.execute(nextAction)
        self.assertEqual(game.getScore(), 23)
        
    def test_generate_maze(self):
        try:
            generator = MazeGenerator()
            maze = generator.create_maze(10, 10)
            fn = "test"
            maze.save(maze, filename=fn)

            # load the new maze
            __ENVIRONMENT__ = "test"
            # display the interface (or not)
            __GUI__ = False

            game = Game(__ENVIRONMENT__, __GUI__)
            # returns a turtle that execute actions on its environment
            turtle = game.start()
            
            # the hard-coded path to find the pizza in the maze environment
            actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]

            i = 0
            while i < 30:
                r = random.randint(0, 3)
                actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
                result = turtle.execute(actions[r])
                i += 1
            self.assertTrue(True)
        except:
            self.assertFalse(True)

    def test_algorithm_assessment(self):
        try:
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

            # create the assessor (nb runs, min height, min width, max height, max width)
            assessor = Assessor(100, 10, 10, 20, 20)
            # provide your solution
            assessor.setSolution(MySolution)
            # run the assessor and wait for your score
            assessor.run()
            self.assertTrue(True)
        except:
            self.assertFalse(True)


class MazeTest(unittest.TestCase):

    def test_maze_generation(self):
        generator = MazeGenerator()
        maze = generator.create_maze(10, 10)
        filepath = "test"
        self.assertEqual(maze.nrows, 10)
        self.assertEqual(maze.ncolumns, 10)


class GameTest(unittest.TestCase):

    def test_game_creation(self):
        __ENVIRONMENT__ = "maze"
        __GUI__ = False

        game = Game(__ENVIRONMENT__, __GUI__)
        turtle = game.start()
        self.assertEqual(turtle.getNumberOfActions(), 0)

if __name__ == '__main__':
    mazeTest = MazeTest()
    unittest.main()