from .game import *
from .mazeGenerator import MazeGenerator
from .assessor import Assessor
import random

def solution(feedback):
    r = random.randint(0, 3)
    actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
    result = actions[r]
    return result

if __name__ == '__main__':
    '''
    # generation of the maze
    generator = MazeGenerator()
    maze = generator.create_maze(10, 10)
    filepath = "test"
    maze.save(maze, filename=filepath)

    # the name of the environment
    __ENVIRONMENT__ = "test"
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
    '''

    assessor = Assessor(10000, 10, 10, 20, 20, 1000)
    assessor.setSolution(solution)
    assessor.run()