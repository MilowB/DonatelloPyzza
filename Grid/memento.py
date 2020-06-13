from map import *

class Memento:
    def __init__(self, state):
        self._state = state

    def getState(self):
        return self._state