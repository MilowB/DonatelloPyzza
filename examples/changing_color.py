import sys
import os
import random
import pygame
import time


sys.path.insert(0, os.path.abspath("donatellopyzza/"))
from enums import Action
from game import *


if __name__ == '__main__':
    __ENVIRONMENT__ = "maze"
    __GUI__ = True

    # Initialiser le jeu
    game = Game(__ENVIRONMENT__, __GUI__)
    turtle = game.start()
    
    # Boucle principale du jeu
    while not game.isWon():
        # Définir les actions que l'agent va exécuter
        actions = [Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.TURN_RIGHT,
                   Action.MOVE_FORWARD, Action.MOVE_FORWARD, Action.MOVE_FORWARD]

        squares = game.getSquaresDict()
        textSquares = {}
        for key in squares:
            # Générer une couleur aléatoire pour la case actuelle de l'agent
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = pygame.Color(r, g, b, 255)
            squares[key] = pygame.Color(r, g, b, 255)
            textSquares[key] = f"({key[0]}, {key[1]})"
            

        # Mettre à jour la couleur de la case actuelle
        game.setSquaresColors(squares)
        game.setSquaresText(textSquares)     

        for a in actions:
            # Obtenir la position actuelle de l'agent
            position = turtle.agent.getCurrentPosition()
            x, y = position.x, position.y
            
            #create a  with the position as key and the color as value
            key = (x, y)
            random_txt = 'update'
            print(f"random_txt: {random_txt}")
            color = pygame.Color(255, 0, 0, 255)
            game.updateSquareColor(key, color)
            game.updateSquareText(key, random_txt)
            # Exécuter l'action
            result, _ = turtle.execute(a)
            # Attendre un peu pour rendre le déplacement visible
            time.sleep(1)
