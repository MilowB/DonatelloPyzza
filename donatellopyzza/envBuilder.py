import os, sys, inspect
import pkg_resources
from pathlib import Path
from pkg_resources import resource_string

#Pour inclure les fichiers de l'environnement
cmd_subfolder_grid = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

from test import Test
from parser import Parser
from grid import Grid


class EnvBuilder:
    def __init__(self, name: str, gui: bool):
        self.name = name
        self.gui = gui

    def get_data_path(self, path):
        
        return pkg_resources.resource_filename(__name__, path + self.name)

    def build_grid(self):
        data_path = self.get_data_path("data/environments/")
        parser = Parser(data_path)
        gui, map, agents = parser.parse()
        # for simplicity matters, we only use one agent in this package
        return agents[0], Grid(gui, map, agents, self.gui, self.name)
