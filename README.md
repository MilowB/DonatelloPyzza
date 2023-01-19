## DonatelloPyzza

A simple environment to help beginners learn Python in high school and at the university.
A turtle can move through a grid and touch each cell until it finds the pizza.
This game can be used at several levels:
- for young beginners: they can hard-code a path to help the turtle find its pizza
- for beginners: they can develop intuitive heuristics to find the pizza
- for intermediate or advanced developers: they can develop a complex path finding method or AI-based solutions.

You can manually create the grid world in which the turtle moves. Soon you will be able to generate new environements automatically through the game API.

![View of the game](views/example.gif)


## Installation

`pip install -r requirements.txt`

`pip install donatellopyzza`


## Getting started

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


Now you know how to play, let's create the game and its environment:

First, import the right modules to run the game:

```python
from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
```

`Game` is a class that you will use to create a game instance

```python
# specify the name of the environment
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
feedback = turtle.execute(Action.FORWARD)
print(feedback)
```

You can use the feedback from the `execute()` method to see what happened after your action.

For more details, you can find several complete examples of the game loop in the `examples` folder on the github repository for this project.

Have fun!


## What's new

- 2023-01-17 (v1.2)
    Initial release


## Roadmap

    - add a gridworld generator