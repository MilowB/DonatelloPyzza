# wrapper class including the agents and the environment
# avoid having to manipulate the environment by yourself
class Turtle:

    def __init__(self, agent, env):
        self.env = env
        self.agent = agent
        self.env.nbActions = 0

    def execute(self, action):
        feedback = self.env.step(self.agent, action)
        return feedback

    def getNumberOfActions(self):
        return self.env.nbActions
