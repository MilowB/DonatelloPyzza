from random import randint
import sys, pygame
import pkg_resources
import math

class GUI:
    def __init__(self, height, width):
        pygame.init()
        self.squareToDisplay = []
        self.agentToDisplay = []
        self.height = height
        self.width = width
        self.squareWidth = 75
        self.disp = False
        self.colors = []
        self.shadeColors = []
        path = pkg_resources.resource_filename(__name__, "../data/images/pizza.png")
        self.pizza = pygame.image.load(path)
        for i in range(height * width):
            r = randint(15, 255)
            g = randint(0, 160)
            b = randint(0, 255)
            sr = r - 15
            self.colors.append(pygame.Color(r, g, b, 255))
            self.shadeColors.append(pygame.Color(sr, g, b, 255))
        self.endCt = 0

    def scale(self, value):
        res = int(1 / (math.sqrt(value) + 1) * 1100)
        return res

    '''
    Objectif : Mettre a jour l'image
    Param : map - la grille
    '''
    def update(self, map):
        self.squareWidth = self.scale(len(self.squareToDisplay))
        self.squareToDisplay = []
        self.agentToDisplay = []
        for square in map.squares:
            self.square(square.end, square.color, square._char, (square.x * self.squareWidth) - self.squareWidth, (square.y * self.squareWidth) - self.squareWidth, square.touched)
            for ag in square._filled:
                self.agent(square, ag)

    '''
    Objectif : Ajoute un carre a la liste d'affichage
    Param : Int, Int, Int - w, le type de case (mur ou pas), x, y, les coordonnees de la case
    '''
    def square(self, end, color, w, x, y, touched):
        width = self.squareWidth

        col = -1
        if end:
            col = color
            
        if touched:
            self.touchedSquare(x, y, self.squareWidth - 1, self.squareWidth - 1)
        elif w == "B":
            self.wall(x, y, self.squareWidth - 1, self.squareWidth - 1)
        else:
            self.squareToDisplay.append([col, (x ,y, width, width)])

    '''
    Objectif : Change le design de la case lorsque c'est un mur
    Param : Int, Int, Int, Int - x, y, les coordonnees de la case, width, height, les dimensions de la case
    '''
    def wall(self, x, y, width, heigth):
        color = -2
        self.squareToDisplay.append([color, (x ,y, width, heigth)])

    def touchedSquare(self, x, y, width, heigth):
        color = -3
        self.squareToDisplay.append([color, (x ,y, width, heigth)])

    '''
    Objectif : Ajout un agent a la liste d'affichage
    Param : Square - la case sur laquelle dessiner l'agent
    '''
    def agent(self, square, agent):
        marge = 0
        self.agentToDisplay.append([agent, (marge + (square.x * self.squareWidth) - self.squareWidth, marge + (square.y * self.squareWidth) - self.squareWidth)])

    '''
    Objectif : Afficher les donnees presentent dans les listes d'affichages (cases et agents)
    '''
    def display(self):
        squareWidth = self.scale(len(self.squareToDisplay))
        self.endCt = 0
        if not self.disp:
            size = width, height = self.height * squareWidth, self.width * squareWidth
            self.screen = pygame.display.set_mode(size)
            pygame.display.set_caption("DonatelloPyzza")
            self.disp = True
        black = 0, 0, 0
        green = pygame.Color(0, 180, 0, 255)
        self.screen.fill(black)
        for i in range(len(self.squareToDisplay)):
            color = pygame.Color(0, 180, 0, 255)
            if not self.squareToDisplay[i][0] is None:
                if self.squareToDisplay[i][0] > -1:
                    color = self.shadeColors[self.squareToDisplay[i][0]]
                elif self.squareToDisplay[i][0] == -2:
                    color = pygame.Color(255, 255, 255, 255)
                elif self.squareToDisplay[i][0] == -3:
                    color = pygame.Color(0, 0, 200, 255)
            pygame.draw.rect(self.screen,  color, self.squareToDisplay[i][1], 0)
            if self.squareToDisplay[i][0] is None:
                self.pizza = pygame.transform.scale(self.pizza, (squareWidth, squareWidth))
                self.screen.blit(self.pizza, self.squareToDisplay[i][1])
        for i in range(len(self.agentToDisplay)):
            self.agentToDisplay[i][0].draw(self.screen, self.agentToDisplay[i][1], squareWidth)
        pygame.display.flip()