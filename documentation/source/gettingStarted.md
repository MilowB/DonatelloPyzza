# Installation

This package can be easily installed through `pip`. If you do not know what is pip or if it is not installed on your machine, you should first read this page:

[https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

Otherwise, you are ready to install Donatello Pyzza!

`pip install donatellopyzza`


# Getting started

Now Donatello Pyzza has been installed, let's see how to use it. First, import the minimum modules to run the game:

```python
from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
```

`Game` is a class that we use to create a game instance. `Action` and `Feedback` are two classes used to describe game events. We will come back to these classes later.

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

The previous code initialize the game and start it. Once the game has started, you get a turtle instance which you can move around the board.
To do this, the following instruction can be used:

```python
feedback = turtle.execute(Action.MOVE_FORWARD)
print(feedback)
```

You can print the feedback returned from the `execute()` method to see what happened after your action. 
As you can see, this code only move your turtle one time. You can write a loop around the `turtle.execute(Action.MOVE_FORWARD)` call to watch your turtle move several times.
To illustrate, you can use the `game.isWon()` method to ensure to loop on the `turtle.execute()` until the turtle find the pizza.

```python
while not game.isWon():
    feedback = turtle.execute(Action.MOVE_FORWARD)
    print(feedback)
```

# Learning the rules:  actions and feedbacks

Let's speak about `Action` and `Feedback`. They simply define the different actions and feedbacks types. You can use the following actions in your code:

    Action.MOVE_FORWARD -> make your turtle go one step forward
    Action.TURN_RIGHT -> your turtle will turn on its right
    Action.TURN_LEFT -> on its left
    Action.TOUCH -> the turtle will touch the cell in front of it to know its type


Depending on your action, the game can provide you one of the following feedback:

    Feedback.COLLISION -> you just tried to walk in a wall !
    Feedback.MOVED -> you successfully moved
    Feedback.MOVED_ON_PIZZA -> your turtle is on the pizza (congratulations!)
    Feedback.TOUCHED_WALL -> you just touched a wall
    Feedback.TOUCHED_NOTHING -> the touched cell is empty (no wall, no pizza, you can walk on it)
    Feedback.TOUCHED_PIZZA -> the turtle touched the pizza


# Testing the full code


You can copy and paste the full code of this example and try it on your machine.

```python
from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback

# specify the name of the maze
__ENVIRONMENT__ = "line"
# display the interface (or not)
__GUI__ = True

game = Game(__ENVIRONMENT__, __GUI__)
# returns a turtle that execute actions on its environment
turtle = game.start()

while not game.isWon():
   feedback = turtle.execute(Action.MOVE_FORWARD)
```

Congratulations, you found the pizza with 4 movements!

You can find more examples in the `Tutorials` section of this documentation. They will present more advanced functionnalities of this package.