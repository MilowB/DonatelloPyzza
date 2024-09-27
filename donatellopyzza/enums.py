from enum import Enum

class Action(Enum):
    MOVE_FORWARD = 0, "Move_forward"
    TURN_RIGHT = 1, "Turn_right"
    TURN_LEFT = 2, "Turn_left"
    TOUCH = 3, "Touch"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

    def __eq__(self, act):
        try:
            return self.value == act.value
        except:
            return False

# TODO: remove duplicate in grid.py
class Feedback(Enum):
    NO_FEEDBACK = -1, "No_feedback"
    COLLISION = 0, "Collision"
    MOVED = 1, "Moved"
    MOVED_ON_PIZZA = 2, "Moved_on_pizza"
    TOUCHED_WALL = 3, "Touched_wall"
    TOUCHED_NOTHING = 4, "Touched_nothing"
    TOUCHED_PIZZA = 5, "Touched_pizza"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value

    def __eq__(self, fb):
        try:
            return self.value == fb.value
        except:
            return False