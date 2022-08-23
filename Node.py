import math

grid_size = 100


class Node:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.g = math.inf
        self.rhs = math.inf
        self.bptr = None
        self.nbrs = [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
        self.nbrs = list(filter(lambda pos: 0 <= pos[0] <= grid_size and 0 <= pos[1] <= grid_size, self.nbrs))

    def __str__(self):
        return str(self.pos)

    def __eq__(self, other):
        return self.pos == other.pos

    def dist_to(self, other):
        return math.dist(self.pos, other.pos)
