import os, sys, inspect
from envBuilder import *
import time
import random

'''
Actions
-------
0 - forward
1 - backward
2 - left rotation
3 - right rotation
'''


# wrapper class including the agents and the environment
# avoid having to manipulate the environment by yourself
class Turtle:

    def __init__(self, agent, env):
        self.env = env
        self.agent = agent

    def execute(self, action):
        return self.env.step(self.agent, action)