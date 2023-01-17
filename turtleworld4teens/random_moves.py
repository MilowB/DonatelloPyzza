from game import Game
import time
import random

if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    i = 0
    while i < 10:
        time.sleep(0.3)
        random_action = random.randint(0, 3)
        # actions are integers in [0,3], see the documentation to know their meaning
        result = turtle.execute(random_action)
        i += 1