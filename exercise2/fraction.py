from astar import *

goal = 1/8

class FractionSearchNode(SearchNode):
    def __init__(self, state, level):
        h = 1
        isGoal = int(state[:4])/int(state[4:]) == goal
        self.g = 1
        self.level = level
        SearchNode.__init__(self, state, [], h, isGoal)


    def expandNode(self):
        if self.level <= 7:
            for i in range(len(self.state)):
                if i == self.level:
                    continue
                charAtLvl = self.state[self.level]
                charAtI = self.state[i]
                childState = list(self.state)
                childState[self.level] = charAtI
                childState[i] = charAtLvl
                self.children.append(FractionSearchNode("".join(childState),self.level+1))
        else:
            pass

start = FractionSearchNode('314725896', 0)

print(aStarSearch(start))
