# DonatelloPyzza

A simple environment to help teenagers learning Python in high school. 
A turtle can move in a grid and touch each cell until it finds the salad.

You can manually create the grid world in which the turtle is moving or generate it automatically (soon).

# Documentation

First, import the right modules to run the game:

    from donatellopyzza import Game
    from donatellopyzza import Action
    from donatellopyzza import Feedback

`Game` is a class that you will use to create a game instance. `Action` and `Feedback` define the different action and feedback types. You can use the following actions in your code:


    FORWARD -> make your turtle go one step forward
    TURN_RIGHT -> your turtle will turn on its right
    TURN_LEFT -> on its left
    TOUCH -> the turtle will touch the cell in front of it to know its type


Depending on your action, the game can provide you on of the following feedback:


    COLLISION -> you just tried to walk in a wall !
    MOVED -> you successly moved
    IS_ON_PIZZA -> your turtle is on the pizza (congratulation!)
    TOUCHED_WALL -> you just touched a wall
    TOUCHED_NOTHING -> the touched cell is empty (no wall, no pizza, you can walk on it)
    TOUCHED_PIZZA -> the turtle touched the pizza


Now you know how to play, let's create the game and its environment:

        # specify the name of the environment
        __ENVIRONMENT__ = "hard_maze"
        # display the interface (or not)
        __GUI__ = True

        game = Game(__ENVIRONMENT__, __GUI__)
        # returns a turtle that execute actions on its environment
        turtle = game.start()
        
Once the game starts, you retrieve a turtle instance that you can move on the board.
To do this, the following instruction can be used:

    feedback = turtle.execute(Action.FORWARD)
    print(feedback)

You can use the feedback of the `execute()` method to know what happened after your action.

For more details, you can find several complete examples of the game loop in the `examples` folder on the github repository of this project.


Have fun!
