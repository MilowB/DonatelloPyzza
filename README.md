# DonatelloPyzza

A simple environment to help beginners learn Python in high school. 
A turtle can move through a grid and touch each cell until it finds the pizza.

You can manually create the grid world in which the turtle moves or generate it automatically (soon).

# Documentation

First, import the right modules to run the game:

    from donatellopyzza import Game
    from donatellopyzza import Action
    from donatellopyzza import Feedback


`Game` is a class that you will use to create a game instance. `Action` and `Feedback` define the different actions and feedbacks types. You can use the following actions in your code:

    FORWARD -> make your turtle go one step forward
    TURN_RIGHT -> your turtle will turn on its right
    TURN_LEFT -> on its left
    TOUCH -> the turtle will touch the cell in front of it to know its type


Depending on your action, the game can provide you on of the following feedback:

    COLLISION -> you just tried to walk in a wall !
    MOVED -> you successfully moved
    IS_ON_PIZZA -> your turtle is on the pizza (congratulation!)
    TOUCHED_WALL -> you just touched a wall
    TOUCHED_NOTHING -> the touched cell is empty (no wall, no pizza, you can walk on it)
    TOUCHED_PIZZA -> the turtle touched the pizza


Now you know how to play, let's create the game and its environment:

    # specify the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
        

Once the game has started, you get a turtle instance which you can move around the board.
To do this, the following instruction can be used:

    feedback = turtle.execute(Action.FORWARD)
    print(feedback)

You can use the feedback from the `execute()` method to see what happened after your action.

For more details, you can find several complete examples of the game loop in the `examples` folder on the github repository for this project.


Have fun!
