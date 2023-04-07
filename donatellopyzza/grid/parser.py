from gui import *
from square import *
from agent import *
from map import *
import sys

class Parser:
    def __init__(self, name):
        self._name = name + ".txt"

    def parse(self):
        m = Map()
        
        file = open(self._name, "r") 
        lines = file.readlines()
        #Terrain
        diff = ord('A') - ord('a')
        yshift = 0
        upSquares = []
        tmpSquares = []
        end = {}
        begin = {}
        agentNb = 0
        for line in lines:
            tmpSquares = []
            yshift += 1
            xshift = 0
            leftSquare = None
            for char in line:
                xshift += 1
                if ord(char) >= ord('A') and ord(char) <= ord('Z') and ord(char) != ord('B'):
                    s = Square(char, xshift, yshift, False, True)
                    end[char] = s
                elif ord(char) >= ord('a') and ord(char) <= ord('z') and ord(char) != ord('p'):
                    s = Square(char, xshift, yshift, True, False)
                    begin[char] = s
                    agentNb += 1
                elif char == "p":
                    s = Square(char, xshift, yshift, False, True)
                    end[char] = s
                else:
                    s = Square(char, xshift, yshift, False, False)
                m.addSquares(s)
                if leftSquare != None:
                    s.neighbors[3] = leftSquare
                    leftSquare.neighbors[1] = s
                if len(upSquares) != 0:
                    s.neighbors[0] = upSquares[xshift - 1]
                    upSquares[xshift - 1].neighbors[2] = s
                tmpSquares.append(s)
                leftSquare = s
            upSquares = list(tmpSquares)

        #Petite verif sur les donnees values
        if agentNb <= 0:
            print("Aucun point de depart pour les agents")
            sys.exit()            
        #Mise en place de l'agent
        agents = []
        for i in range(agentNb):
            agents.append(Agent("00" + str(i + 1), list(begin.values())[i], list(end.values())[i], i))

        m.seatAgents(agents)
        m.countAgents()
        
        g = GUI(xshift, yshift)

        return g, m, agents

    def parse_string(self, str_map):
        m = Map()
        
        lines = str_map.split("\n")
        #Terrain
        diff = ord('A') - ord('a')
        yshift = 0
        upSquares = []
        tmpSquares = []
        end = {}
        begin = {}
        agentNb = 0
        for line in lines:
            tmpSquares = []
            yshift += 1
            xshift = 0
            leftSquare = None
            for char in line:
                xshift += 1
                if ord(char) >= ord('A') and ord(char) <= ord('Z') and ord(char) != ord('B'):
                    s = Square(char, xshift, yshift, False, True)
                    end[char] = s
                elif ord(char) >= ord('a') and ord(char) <= ord('z'):
                    s = Square(char, xshift, yshift, True, False)
                    begin[char] = s
                    agentNb += 1
                elif char == "E":
                    s = Square(char, xshift, yshift, False, True)
                    end[char] = s
                else:
                    s = Square(char, xshift, yshift, False, False)
                m.addSquares(s)
                if leftSquare != None:
                    s.neighbors[3] = leftSquare
                    leftSquare.neighbors[1] = s
                if len(upSquares) != 0:
                    s.neighbors[0] = upSquares[xshift - 1]
                    upSquares[xshift - 1].neighbors[2] = s
                tmpSquares.append(s)
                leftSquare = s
            upSquares = list(tmpSquares)

        #Petite verif sur les donnees values
        if agentNb <= 0:
            print("Aucun point de depart pour les agents")
            sys.exit()            
        #Mise en place de l'agent
        agents = []
        for i in range(agentNb):
            agents.append(Agent("00" + str(i + 1), list(begin.values())[i], list(end.values())[i], i))

        m.seatAgents(agents)
        m.countAgents()
        
        g = GUI(xshift, yshift)

        return g, m, agents 