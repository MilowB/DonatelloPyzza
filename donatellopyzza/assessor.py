from random import randint
from tqdm import tqdm
import os, sys
import time

sys.path.insert(0, 'donatellopyzza/')

from .mazeGenerator import MazeGenerator
from .game import Feedback
from .game import Game


class Assessor:
    def __init__(self, nruns: int, minrows: int, mincolumns: int, maxrows: int, maxcolumns: int, overflow: int):
        assert nruns > 0 and minrows > 7 and mincolumns > 7, "Please, specify a valid number of runs, rows and columns"
        self.func = None
        self.overflow = overflow
        self.nruns = nruns
        self.minrows = minrows
        self.mincolumns = mincolumns
        self.maxrows = maxrows
        self.maxcolumns = maxcolumns
        self.generator = MazeGenerator()

    def setSolution(self, func):
        self.func = func

    def run(self):
        assert self.func != None, "Please, set your solution before running the assessor"
        print("Running the evaluation...")

        success = 0
        failure = 0
        startTime = time.time()
        for i in tqdm(range(self.nruns)):
            r, c = randint(self.minrows, self.maxrows), randint(self.mincolumns, self.maxcolumns)
            a = int(min(r, c) + (abs(r-(r+c)/2)/2))
            b = int(max(r, c) - (abs(c-(r+c)/2)/2))
            maze = self.generator.create_maze(a, b)
            filepath = "assessment_maze"
            maze.save(maze, filename=filepath)       
            game = Game(filepath, False)
            # returns a turtle that execute actions on its environment
            turtle = game.start()
            feedback = None
            cnt = 0
            while not game.isWon(False) and self.overflow > cnt:
                action = self.func(feedback)
                feedback = turtle.execute(action)
                cnt += 1
            if self.overflow > cnt:
                success += 1
            else:
                failure += 1
        endTime = time.time()
        duration = endTime - startTime
        print("Total duration: ", duration, " seconds")
        print("Failed: ", failure, "/", success + failure)