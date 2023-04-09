from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
from donatellopyzza import MazeGenerator
import random
import time


if __name__ == '__main__':
    # generate and save a new random maze
    generator = MazeGenerator()
    maze = generator.create_maze(10, 10)
    fn = "test"
    maze.save(maze, filename=fn)

    # load the new maze
    __ENVIRONMENT__ = "test"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    # the hard-coded path to find the pizza in the maze environment
    actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]

    i = 0
    while i < 15:
        time.sleep(0.3)
        r = random.randint(0, 3)
        actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
        result = turtle.execute(actions[r])
        i += 1