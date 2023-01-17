import os, sys, pygame
from random import randint
import pkg_resources

class Pizza:
    def __init__(self, name, begin, color):
        self._name = name
        self.orientation = Orientation.NORTH
        self.num = id(self)
        self.begin = begin
        self.color = color
        self.position = None
        path = pkg_resources.resource_filename(__name__, "../data/images/pizza.png")
        self.pizza = pygame.image.load(path)

    def setCurrentPosition(self, position):
        self.position = position

    def getCurrentPosition(self):
        return self.position

    def draw(self, screen, xy):
        screen.blit(self.pizza, xy)