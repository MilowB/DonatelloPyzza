from random import randint
from tqdm import tqdm
import time

sys.path.insert(0, 'donatellopyzza/')

from mazeGenerator import MazeGenerator
from game import Feedback
from game import Game


class Assessor:
    def __init__(self, nruns: int, minrows: int, mincolumns: int, maxrows: int, maxcolumns: int):
        assert nruns > 0 and minrows > 0 and mincolumns > 0, "Please, specify a valid number of runs, rows and columns"
        self.func = None
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
        r, c = randint(self.minrows, self.maxrows), randint(self.mincolumns, self.maxcolumns)
        maze = generator.create_maze(r, c)

        success = 0
        failure = 0
        startTime = time.time()
        for i in tqdm(range(self.nruns)):
            feedback = None
            while not game.isWon():
                action = self.func(feedback)
                feedback = turtle.execute(action)
            success += 1
        endTime = time.time()
        duration = endTime - startTime
        print("Total duration: ", duration, " seconds")
        print("Failed: ", failure, "/", success + failure)