from .game import *
from .mazeGenerator import Maze
import random
import time


if __name__ == '__main__':
    # generation of the maze
    maze = Maze.create_maze(10, 10)
    filepath = "test33"
    maze.save(maze, filename=filepath)

    # the name of the environment
    __ENVIRONMENT__ = "test33"
    # display the interface (or not)
    __GUI__ = True


    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    while not game.isWon():
        time.sleep(0.3)
        r = random.randint(0, 3)
        actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
        result = turtle.execute(actions[r])
