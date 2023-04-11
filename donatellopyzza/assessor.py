from random import randint
from tqdm import tqdm
import os, sys
import time

#sys.path.insert(0, os.path.abspath('donatellopyzza/'))

from .mazeGenerator import MazeGenerator
from .game import Feedback
from .game import Game


class Assessor:
    def __init__(self, nruns: int, minrows: int, mincolumns: int, maxrows: int, maxcolumns: int, complexity=0, overflow=-1):
        assert nruns > 0 and minrows > 7 and mincolumns > 7, "Please, specify a valid number of runs, rows and columns"
        if overflow == -1:
            overflow = maxrows * maxcolumns * 2
        self.clss = None
        self.overflow = overflow
        self.nruns = nruns
        self.minrows = minrows
        self.mincolumns = mincolumns
        self.maxrows = maxrows
        self.maxcolumns = maxcolumns
        self.complexity = complexity
        self.generator = MazeGenerator()

    def setSolution(self, clss):
        self.clss = clss

    def run(self):
        assert self.clss != None, "Please, set your solution before running the assessor"
        print("Running the evaluation...")

        success = 0
        failure = 0
        startTime = time.time()
        totalActions = 0
        for i in tqdm(range(self.nruns)):
            r, c = randint(self.minrows, self.maxrows), randint(self.mincolumns, self.maxcolumns)
            deviation = (abs(c-(r+c)/2)/2)
            a = int(min(r, c) + deviation)
            b = int(max(r, c) - deviation)
            maze = self.generator.create_maze(a, b, self.complexity)
            filepath = "assessment_maze"
            maze.save(maze, filename=filepath)       
            game = Game(filepath, False)
            # returns a turtle that execute actions on its environment
            turtle = game.start()
            feedback = Feedback.NO_FEEDBACK
            cnt = 0
            solutionInstance = self.clss()
            while not game.isWon(False) and self.overflow > cnt:
                action = solutionInstance.nextAction(feedback)
                feedback = turtle.execute(action)
                cnt += 1
            totalActions += cnt
            if self.overflow > cnt:
                success += 1
            else:
                failure += 1
        endTime = time.time()
        duration = endTime - startTime
        print("Total duration: ", round(duration, 2), " seconds")
        print("------------------------")
        print("| Success rate: ", round(success / (success + failure), 2) * 100, "% |")
        print("------------------------")
        print("Number of actions per maze: ", round(totalActions/self.nruns, 2))
        print("Time per maze: ", round(duration/self.nruns, 2), "seconds")
        print("------------------------")
