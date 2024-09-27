from turn import *
from orientation import *

class Feedback(Enum):
    COLLISION = 0, "Collision"
    MOVED = 1, "Moved"
    MOVED_ON_PIZZA = 2, "Moved_on_pizza"
    TOUCHED_WALL = 3, "Touched_wall"
    TOUCHED_NOTHING = 4, "Touched_nothing"
    TOUCHED_PIZZA = 5, "Touched_pizza"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

    def __eq__(self, fb):
        return self.value == fb.value

class Map:
    def __init__(self):
        self.num = id(self)
        self.squares = []
        self.numbAgents = 0
        self.askForReset = []


    '''
    Objectif : Calculer le nombre max d'actions à réaliser pour
               aller de la position initiale à la pizza
    Param : Int - Nombre d'actions
    '''
    def getMaxActions(self):
        pass

    '''
    Objectif : Ajouter une case
    Param : Square - case a ajouter a la map
    '''
    def addSquares(self, square):
        self.squares.append(square)

    '''
    Objectif : Recuperer une case de la grille
    Param : Int, Int - la position x, y de la case demandee
    Retour : La case demandee, None si la case est introuvable
    '''
    def get(self, x, y):
        for sq in self.squares:
            if sq.x == x and sq.y == y:
                return sq
        return None

    '''
    Objectif : Placer les agents sur leur point de depart
    Param : agents - les agents a placer
    '''
    def seatAgents(self, agents):
        self.numbAgents = 0
        for agent in agents:
            sq = agent.begin
            sq.fill(agent)
            self.numbAgents += 1

    '''
    Objectif : Search the square where is the agent
    Param : agent - agent whose the position we want to know
    Return : the square where is the agent
    '''
    def getAgentCell(self, agent):
        for sq in self.squares:
            if sq.isHere(agent):
                return sq
        return None

    '''
    directions : 
    0 - haut
    1 - droite
    2 - bas
    3 - gauche
    Retour : Square - case sur laquelle est l'agent après son déplacement
    '''
    def moveAgent(self, agent):
        self.notTouched()
        direction = None
        ori = agent.orientation
        if ori == Orientation.NORTH:
            direction = 0
        elif ori == Orientation.EAST:
            direction = 1
        elif ori == Orientation.SOUTH:
            direction = 2
        elif ori == Orientation.WEST:
            direction = 3

        for sq in self.squares:
            if sq.isHere(agent):
                if sq.neighbors[direction] != None and sq.neighbors[direction].block != "B":
                    sq.neighbors[direction].fill(agent)
                    sq.unfill(agent)
                    return sq.neighbors[direction]
                return sq

    '''
    Objectif : Tourner l'agent dans la direction voulue
    Param : Agent - agent à tourner, Orientation - direction dans laquelle tourner l'agent
    '''
    def turnAgent(self, agent, orientation):
        self.notTouched()
        if orientation == Turn.RIGHT:
            new_orientation = agent.orientation.value + 1
        elif orientation == Turn.LEFT:
            new_orientation = agent.orientation.value - 1
        if new_orientation < 0:
            new_orientation = 3
        elif new_orientation > 3:
            new_orientation = 0
        agent.turn(new_orientation)
    
    '''
    directions : 
    0 - haut
    1 - droite
    2 - bas
    3 - gauche
    Retour : Square - case que l'agent a touché
    '''
    def touch(self, agent):
        direction = None
        ori = agent.orientation
        if ori == Orientation.NORTH:
            direction = 0
        elif ori == Orientation.EAST:
            direction = 1
        elif ori == Orientation.SOUTH:
            direction = 2
        elif ori == Orientation.WEST:
            direction = 3

        for sq in self.squares:
            if sq.isHere(agent):
                if sq.neighbors[direction] != None:
                    self.notTouched()
                    sq.neighbors[direction].touched = True
                    return sq.neighbors[direction]
                return None

    '''
    Objectif : Remet tous les touched à False
    '''
    def notTouched(self):
        for sq in self.squares:
            sq.touched = False

    '''
    Objectif : @debug
    Retour : Int - nombre d'agents
    '''
    def countAgents(self):
        counter = 0
        for sq in self.squares:
            for a in sq._filled:
                counter += 1
        return counter

    '''
    Objectif : Indique si un agent est sur l'objectif
    Param : agent - agent dont on veut avoir l'information
    Retour : Booleen True si l'agent est sur l'objectif, False sinon
    '''
    def isOnEnd(self, agent):
        for sq in self.squares:
            if sq.isHere(agent) and sq.end is True:
                return True
        return False

    '''
    Objectif : Reinitialiser la position de tous les agents lorsque ceux-ci ont atteint l'objectif
    Param : agent - agent dont la position doit etre reinitialisee, agents - ensemble des agents de la grille
    '''
    def restart(self, agent, agents):
        if agent not in self.askForReset:
            self.askForReset.append(agent)
        if len(self.askForReset) >= self.numbAgents:
            for a in self.askForReset:
                for sq in self.squares:
                    if sq.isHere(a):
                        sq.unfill(a)
            self.askForReset = []
                          
            self.seatAgents(agents)
        
    '''
    Objectif : Indique le numero de case sur laquelle se trouve un agent
    Param : agent - agent dont on veut connaitre la case
    Retour : Square - le numero de case de l'agent
    '''
    def agentNumSquare(self, agent):
        for sq in self.squares:
            if sq.isHere(agent):
                return sq

    '''
    Objectif : Indique la case sur laquelle se trouve un agent
    Param : agent - agent dont on veut connaitre la case
    Retour : Square - la case de l'agent
    '''
    def agentSquare(self, agent):
        for sq in self.squares:
            if sq.isHere(agent):
                return sq

    '''
    Objectif : Calcule la recompense donnee a un agent
    Param : agent - agent dont la recopense doit etre calculee
    Retour : Int - recompense donnee a l'agent
    '''
    def calculateReward(self, agent, collision):
        reward = -1
        if self.isOnEnd(agent):
            reward = 1
        elif collision == Feedback.COLLISION:
            reward=  -2
        return reward
        


    '''
    Objectif : Indique si l'agent est en collision avec un autre agent
    Param : agent - agent dont on verifie la collision
    Retour : Int - 1 si collision, 0 sinon
    '''
    def hasCollide(self, agents, agent):
        if self.isOnEnd(agent):
            return 0
        for sq in self.squares:
            if sq.isHere(agent):
                if not sq.end and len(sq._filled) > 1:
                    return 1
        for ag1 in agents:
            for ag2 in agents:
                if (ag1.num == agent.num or ag2.num == agent.num) and ag1.num != ag2.num:
                    if ag1.getCurrentPosition() == ag2.getLastPosition() and ag1.getLastPosition() == ag2.getCurrentPosition():
                        #print("Collision inversion de places") # @debug
                        return 1
        return 0

    '''
    Objectif : Cherche les collisions
    Retour : [[Agent, Agent][Agent, Agent]] - Tableaux d'agents, chaque agents dans un sous tableau sont en collisions entre eux
    '''
    def searchCollisions(self, agents):
        collisions = []
        for sq in self.squares:
            if not sq.end and len(sq._filled) > 1:
                agentsConcerned = []
                for agent in sq._filled:
                    agentsConcerned.append(agent)
                collisions.append(agentsConcerned)

        for ag1 in agents:
            for ag2 in agents:
                if ag1.num != ag2.num:
                    agentsConcerned = []
                    if ag1.getCurrentPosition() == ag2.getLastPosition() and ag1.getLastPosition() == ag2.getCurrentPosition():
                        #print("Collision inversion de places") # @debug
                        agentsConcerned.append(ag1)
                        agentsConcerned.append(ag2)
                        collisions.append(agentsConcerned)
                    
        return collisions
    
    '''
    Objectif : Calcule la recompense donnee a un agent
    Param : agent - agent dont la recopense doit etre calculee
    Retour : Int - recompense donnee a l'agent
    '''
    def isDone(self, agent):
        for sq in self.squares:
            if sq.isHere(agent) and sq == agent.end:
                return True
        return False

    '''
    Objectif : Replace l'agents apres la collision sur son ancienne case
    Param : Agents - l'agents a replacer
    Retour : Square - case actuelle sur laquelle est l'agent
    '''
    def replaceAgents(self, agent):
        for sq in self.squares:
            if sq.isHere(agent):
                sq.unfill(agent)
        for sq in self.squares:
            if agent.getLastPosition() == sq.num:
                sq.fill(agent)
                return sq

    '''
    Objectif : Change la position de l'état objectif vers une case vide
    Param : Square - case sur laquelle poser l'objectif
    '''
    def moveObjOnEmptySquare(self):
        sq = None
        for square in self.squares:
            if square.block != "B" and not square.end and square.isEmpty():
                sq = square
                break
        return sq

    '''
    Objectif : Change la position de l'état objectif
    Param : Square - case sur laquelle poser l'objectif
    '''
    def _moveObjective(self, sq):
        for square in self.squares:
            if square.end:
                square = False
        sq.end = True

    '''
    Objectif : 
    Param : Square - case sur laquelle poser l'objectif
    '''
    def isOnObjective(self, agent):
        for sq in self.squares:
            if sq.isHere(agent) and sq.end:
                return True
            else:
                return False


    '''
    Objectif : @debug
    Param : Int - numero du square dont on veut la position
    Retour : String - position du square sous forme (x, y)
    '''
    def squarePosition(self, numSquare):
        for sq in self.squares:
            if sq.num == numSquare:
                return "(" + str(sq.x) + ", " + str(sq.y) + ")"

