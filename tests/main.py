from donatellopyzza import MazeGenerator
from donatellopyzza import Game
import unittest

class MazeTest(unittest.TestCase):

    def isAllocated(x):
        print(x)

    def test_maze_generation(self):
        generator = MazeGenerator()
        maze = generator.create_maze(10, 10)
        filepath = "test"
        self.assertEqual(maze.nrows, 10)
        self.assertEqual(maze.ncolumns, 10)

        np.apply_along_axis(isAllocated, axis=1, arr=myarray)

        self.assertEqual('foo'.upper(), 'FOO')


class GameTest(unittest.TestCase):

    def test_game_creation(self):
        __ENVIRONMENT__ = "maze"
        __GUI__ = False

        game = Game(__ENVIRONMENT__, __GUI__)
        turtle = game.start()
        self.assertEqual(turtle.getNumberOfActions(), 0)

if __name__ == '__main__':
    mazeTest = MazeTest()
    unittest.main()