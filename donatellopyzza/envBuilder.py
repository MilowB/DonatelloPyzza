import os, sys, inspect
import pkg_resources
from pathlib import Path
from pkg_resources import resource_string

sys.path.insert(0, os.path.abspath("donatellopyzza/grid/"))

from grid import Grid
from mazeParser import Parser


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
