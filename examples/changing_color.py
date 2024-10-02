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

        for a in actions:
            # Obtenir la position actuelle de l'agent
            position = turtle.agent.getCurrentPosition()
            x, y = position.x, position.y

            # Générer une couleur aléatoire pour la case actuelle de l'agent
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = pygame.Color(r, g, b, 255)


            # Mettre à jour la couleur de la case actuelle
            game.setSquareColor((x, y), color)

            # Mettre à jour le texte de la case avec les coordonnées de l'agent
            text = f"({x}, {y})"
            game.setSquareText((x, y), text)        
            
            
            # Exécuter l'action
            result, _ = turtle.execute(a)
            


            

            # Attendre un peu pour rendre le déplacement visible
            time.sleep(3)
