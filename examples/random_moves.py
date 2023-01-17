from game import Game
import time
import random


def main():
    # Afficher ou non l'interface
    __ENVIRONMENT__ = "maze"
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    turtle = game.start()
    
    i = 0
    while i < 10:
        time.sleep(0.3)
        random_action = random.randint(0, 3)
        result = turtle.execute(random_action)
        i += 1

if __name__ == '__main__':
    main()