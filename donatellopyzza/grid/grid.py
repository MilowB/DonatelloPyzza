from map import *
from gui import *
from turn import *
import pygame

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

class Grid:
    def __init__(self, g, m, a, d, name):
        self.display = d
        self._name = name
        self.action_space = 2
        self.gui = g
        self.map = m
        self.debug = False
        self.agents = a
        self.nbActions = 0
        self.foundPizza = False

    '''
    Objectif : Fait executer a l'agent une action
    Param : agent - l'agent qui execute une, action - action que l'agent doit executer
    Retour : résultat du mouvement de l'agent (1 si mur, 2 sinon)
    '''
    def step(self, agent, action):
        assert action != None and action.value < 4, "you tried to execute an invalid action"
        # check the game events before executing a new action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                exit()

        if not type(action) is int:
            action = int(action.value)
        square = None
        square_touched = None
        #Mise a jour de la pile de cases parcourues
        squareTmp = self.map.agentNumSquare(agent)
        agent.savePosition(squareTmp)
        if action < 1:
            square = self.map.moveAgent(agent)
        elif action < 3:
            self.map.turnAgent(agent, Turn(action))
        elif action < 4:
            square_touched = self.map.touch(agent)
        #Mise a jour de la position courante
        agent.setCurrentPosition(square)

        if self.display:
            self.gui.update(self.map)
            self.gui.display()

        result = None
        if self._name == "env1":
            result = self.result_for_env1(square, squareTmp, square_touched, agent)
        else:
            result = self.result_generic_env(square, squareTmp, square_touched, agent, action)

        #if not self.foundPizza:
        self.nbActions += 1

        return result
    
    def pizzaIsFound(self):
        return self.foundPizza

    def disableDisplay(self):
        self.display = False

    def enableDisplay(self):
        self.display = True

    '''
    Objectif : @debug
    '''
    def printQvalues(self, qtable):
        self.map.printQvalues(qtable)

    '''
    Objectif : @debug
    '''
    def countAgents(self):
        return self.map.countAgents()

    '''
    Objectif : @debug
    '''
    def squarePosition(self, numSquare):
        return self.map.squarePosition(numSquare)


    '''
    Objectif : indique le bon retour de l'environnement
    '''
    def result_generic_env(self, square, old_square, square_touched, agent, action):
        if action == 1 or action == 2:
            return Feedback.MOVED
        if not square is None:
            #Si l'agent n'a pas bougé alors il a rencontré un mur
            if square.equal(old_square):
                return Feedback.COLLISION
            elif square.isPizza():
                self.foundPizza = True
                return Feedback.MOVED_ON_PIZZA
            return Feedback.MOVED
        elif not square_touched is None:
            if square_touched.isWall():
                return Feedback.TOUCHED_WALL
            elif square_touched.isPizza():
                return Feedback.TOUCHED_PIZZA
            return Feedback.TOUCHED_NOTHING
        return None


    '''
    Objectif : indique le bon retour de l'environnement spécifiquement par rapport à l'env1
    qui a des règles un peu particulières sur l'alternance e1 / e2
    '''
    def result_for_env1(self, square, old_square, square_touched, agent):
        #Regle de l'environnement : alternance e1 / e2 pour retour r2
        #La case objectif bouge pour de manière à faire apprendre à l'agent cette alternance
        if not square is None:
            if not square.equal(old_square) and self.map.isOnObjective(agent):
                self.map.moveObjOnEmptySquare()
            elif square.equal(old_square) and self.map.isOnObjective(agent):
                pass
            elif square.equal(old_square):
                self.map.moveObjOnEmptySquare()

            #Si l'agent n'a pas bougé alors il a rencontré un mur
            if square.equal(old_square):
                return 1
            return 2
        elif not square_touched is None:
            if square_touched.isWall():
                return 1
            return 2
        return 2