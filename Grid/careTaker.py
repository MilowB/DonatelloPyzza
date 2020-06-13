class CareTaker:
    def __init__(self):
        self._memento = []

    def add(self, memento):
        if len(self._memento) > 2:
            self._memento.pop(0)
        self._memento.append(memento)

    def getLast(self):
        length = len(self._memento)
        return self._memento[length - 1]