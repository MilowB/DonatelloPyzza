## DonatelloPyzza

DonatelloPyzza is a simple and educational game to help beginners learn algorithmic in Python in high school and university.

A turtle can move through a grid and touch each cells until it finds the pizza.
This game can be used at several levels:
- for young beginners: they can hard-code a path to help the turtle find its pizza in small mazes.
- for beginners: they can develop intuitive heuristics to find the pizza
- for intermediate or advanced developers: they can develop a complex path finding method or AI-based solutions.


![View of the game (please go to the homepage of the project to watch this gif)](https://github.com/MilowB/DonatelloPyzza/blob/master/views/example.gif)


## Installation


`pip install donatellopyzza`


## Getting started

First, import the right modules to run the game:

```python
from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
```

`Game` is a class that you will use to create a game instance.

Let's create the game and its environment:

```python
# specify the name of the maze
__ENVIRONMENT__ = "maze"
# display the interface (or not)
__GUI__ = True

game = Game(__ENVIRONMENT__, __GUI__)
# returns a turtle that execute actions on its environment
turtle = game.start()
```

Once the game has started, you get a turtle instance which you can move around the board.
To do this, the following instruction can be used:

```python
feedback, _ = turtle.execute(Action.MOVE_FORWARD)
print(feedback)
```

You can use the feedback from the `execute()` method to see what happened after your action.

Finally, let's run your turtle:

> python yourfile.py

## Learning the rules:  actions and feedbacks

`Action` and `Feedback` define the different actions and feedbacks types. You can use the following actions in your code:

    Action.MOVE_FORWARD -> make your turtle go one step forward
    Action.TURN_RIGHT -> your turtle will turn on its right
    Action.TURN_LEFT -> on its left
    Action.TOUCH -> the turtle will touch the cell in front of it to know its type


Depending on your action, the game can provide you one of the following feedback:

    Feedback.COLLISION -> you just tried to walk in a wall !
    Feedback.MOVED -> you successfully moved
    Feedback.MOVED_ON_PIZZA -> your turtle is on the pizza (congratulation!)
    Feedback.TOUCHED_WALL -> you just touched a wall
    Feedback.TOUCHED_NOTHING -> the touched cell is empty (no wall, no pizza, you can walk on it)
    Feedback.TOUCHED_PIZZA -> the turtle touched the pizza


## Generating and save your own mazes

`Maze` is a class used to generate and save new mazes. You can retrieve saved maze by their names as indicated in example files. A new maze is generated (and saved) as follow:

```python
from donatellopyzza import MazeGenerator

generator = MazeGenerator()
maze = generator.create_maze(10, 10)
fn = "test"
maze.save(maze, filename=fn)
```

For more details, you can find several complete examples of the game loop in the `examples` folder on the github repository of this project. You can also look for the documentation at this [link](https://milowb.github.io/DonatelloDocumentation/html/index.html)

Have fun!


## What's new

- 2024-09-27 (v1.8)
    Add a RLGame class facilitating the use of RL algorithm.
- 2024-09-25 (v1.7)
    Add a reward function in order to play the game with reinforcement learning. Add the possibility to change the color of each cell for debugging.
- 2023-04-09 (v1.6)
    Integration of an algorithm assessment class. Allows to evaluate automatically a solution on several mazes.
- 2023-04-07 (v1.5)
    Integration of a maze generator from Alexandru Văleanu (https://github.com/AlexandruValeanu/Mazify).
- 2023-01-17 (v1.2)
    Initial release


## Roadmap

- make several tests for this package
- make tutorials to help beginners use this package
- make a more formal documentation
- promote this game through a website
- ~~add a RLGame class to facilitate the use of RL algorithm for solving the game~~
- ~~add a reward in the step() method to allow reinforcment learning~~
- ~~adapt the GUI to resize it depending on the number of cells~~
- ~~add a test infrastructure to validate users' algorithm on several mazes~~
- ~~make possible to the user to select the difficulty of the maze when generating it~~
- ~~debug the GUI~~
- ~~add a gridworld generator~~
