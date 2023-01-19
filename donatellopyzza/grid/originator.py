from memento import *
from map import *

class Originator:
    def __init__(self):
        self.state = ""

    def getState(self):
        return self.state
    
    def setState(self, state):
        self.state = state
    
    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.getState()
