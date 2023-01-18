from game import *
import random
import time


if __name__ == '__main__':    
    # the name of the environment
    __ENVIRONMENT__ = envname
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    result = turtle.execute(Action.FORWARD)
    result = turtle.execute(Action.TOUCH)
    print(result)
    time.sleep(0.3)
    result = turtle.execute(Action.FORWARD)
    result = turtle.execute(Action.TOUCH)
    print(result)
    time.sleep(0.3)
    result = turtle.execute(Action.TURN_RIGHT)
    result = turtle.execute(Action.TOUCH)
    print(result)
    time.sleep(0.3) 
    result = turtle.execute(Action.FORWARD)
    print(result)
    time.sleep(0.3)
    result = turtle.execute(Action.FORWARD)
    print(result)
    time.sleep(0.3)
    result = turtle.execute(Action.FORWARD)
    print(result)
    time.sleep(0.3)