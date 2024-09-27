import os, sys
import pygame
from originator import *
from careTaker import *
from orientation import *

from random import randint
import pkg_resources

class Agent:
    def __init__(self, name, begin, end, color):
        self._name = name
        self.orientation = Orientation.NORTH
        self.num = id(self)
        self.begin = begin
        self.end = end
        self.color = color
        self.originator = Originator()
        self.caretaker = CareTaker()
        self.position = None
        path = pkg_resources.resource_filename(__name__, "../data/images/turtle_small.png")
        self.turtle = pygame.image.load(path)
        self.angle = 0

    def setCurrentPosition(self, position):
        self.position = position

    def savePosition(self, square):
        self.originator.setState(square)
        self.caretaker.add(self.originator.saveStateToMemento())

    def turn(self, orientation):
        diff = abs(self.orientation.value - orientation)
        if diff < 2 or diff == 3:
            self.orientation = Orientation(orientation)

    def goBack(self):
        self.originator.getStateFromMemento(self.caretaker.getLast())

    def getLastPosition(self):
        return self.caretaker.getLast().getState()

    def getCurrentPosition(self):
        return self.position

    def getOrientation(self):
        return self.orientation

    def draw(self, screen, xy, scale):
        cste_angle = 90
        new_angle = cste_angle * self.orientation.value
        self.turtle = pygame.transform.scale(self.turtle, (scale, scale))
        self.turtle = pygame.transform.rotate(self.turtle, new_angle - self.angle)
        self.angle = new_angle
        screen.blit(self.turtle, xy)