from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
import random
import time


if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "hard_maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    i = 0
    while i < 15:
        time.sleep(0.3)
        r = random.randint(0, 3)
        actions = [Action.FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
        result = turtle.execute(actions[r])
        print(result)
        i += 1