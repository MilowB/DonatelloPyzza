from enum import Enum

class Action(Enum):
    FORWARD = 0, "Forward"
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