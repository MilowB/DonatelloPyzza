import sys
import os

sys.path.insert(0, os.path.abspath("donatellopyzza/"))
from game import *

from random import randint
import pygame
import time
from enums import Action

if __name__ == '__main__':
    __ENVIRONMENT__ = "maze"
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    turtle = game.start()
    
    while not game.isWon():
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
                   Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]
        for a in actions:
            squares = game.getSquaresDict()

            # Définir les couleurs des carrés
            for key in squares:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                squares[key] = pygame.Color(r, g, b, 255)
            game.setSquaresColors(squares)

            # Définir les textes des carrés
            texts = {}
            for key in squares:
                
                texts[key] = f"Pos {key}"  # Exemple : afficher les coordonnées du carré
            game.setSquaresText(texts)

            result, _ = turtle.execute(a)
            time.sleep(1)
