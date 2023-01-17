import os, sys, inspect

#Pour inclure les fichiers de l'environnement
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

from parser import Parser
from grid import Grid
'''
Objectif :
Parser le bon environnement et retourner les qtables/rewtable a partir du nom passer au constructeur
'''
class EnvBuilder:
    def __init__(self, name: str, gui: bool):
        self.name = name
        self.gui = gui

    def build_grid(self):
        path = "../data/environments/"
        parser = Parser(path + self.name)
        gui, map, agents = parser.parse()
        # for simplicity matters, we only use one agent in this package
        return agents[0], Grid(gui, map, agents, self.gui, self.name)
