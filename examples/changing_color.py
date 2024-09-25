from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback

from random import randint
import pygame
import time

if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    while not game.isWon():
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
            Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
        # execute the path step by step
        for a in actions:
            squares = game.getSquaresDict()
            for key in squares:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                squares[key] = pygame.Color(r, g, b, 255)
            game.setSquaresColors(squares)
            result, _ = turtle.execute(a)
            time.sleep(1)