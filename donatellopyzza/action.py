from enum import Enum

class Action(Enum):
    FORWARD = 0, "Forward"
    TOUCH = 1, "Touch"
    TURN_LEFT = 2, "Turn_left"
    TURN_RIGHT = 3, "Turn_right"

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value