from map import *
from gui import *
from turn import *
import pygame

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
        self.colorSquares = None

    def setSquaresColors(self, colors):
        self.colorSquares = colors

    def getSquaresAsDict(self):
        d = {}
        for square in self.map.squares:
            d[square.position()] = None
        return d

    '''
    Objectif : Add the position to the agent.position
    Param : agent - agent whose we want to know the position
    '''
    def updatePosition(self, agent):
        #Mise a jour de la position courante
        square = self.map.getAgentCell(agent)
        agent.setCurrentPosition(square)

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
        square = self.map.getAgentCell(agent)
        agent.setCurrentPosition(square)

        if self.display:
            self.gui.update(self.map, self.colorSquares)
            self.gui.display()

        result = self.result_generic_env(square, squareTmp, square_touched, agent, action)

        self.nbActions += 1
        reward = self.map.calculateReward(agent, result)
        return result, reward
    
    def pizzaIsFound(self):
        return self.foundPizza

    def disableDisplay(self):
        self.display = False

    def enableDisplay(self):
        self.display = True

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
