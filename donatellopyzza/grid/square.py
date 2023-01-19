class Square:
    '''
    indices neighbors :
    0 - haut
    1 - droite
    2 - bas
    3 - gauche
    '''
    
    def __init__(self, char, x, y, begin, end):
        self.num = str(x) + str(y)
        self.neighbors = [None, None, None, None]
        self.block = char
        self._filled = []
        self.begin = begin
        self.end = end
        self.color = None
        self._char = char
        self.x = x
        self.y = y
        self.touched = False

    def isEmpty(self):
        if len(self._filled) == 0:
            return True
        return False

    def isWall(self):
        if self.block == "B":
            return True
        return False

    def isPizza(self):
        if self.block == "p":
            return True
        return False

    def addNeighbor(self, neigh):
        self.neighbors.append(neigh)

    def fill(self, agent):
        self._filled.append(agent)

    def unfill(self, agent):
        for i in range(len(self._filled)):
            if self._filled[i].num == agent.num:
                self._filled.pop(i)
                break

    def isHere(self, agent):
        for a in self._filled:
            if a.num == agent.num:
                return True
        return False

    def position(self):
        return (self.x, self.y)

    def equal(self, square):
        if self.num == square.num:
            return True
        return False