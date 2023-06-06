import random

"""
This class creates a random maze using Kruskals Algorithm.

returns:
    maze - a set of edges of spanning tree output from Kruskals
    edgeWeights - for the solver, it is the same as maze but includes weights
"""


class Generator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes, self.edges = self.graph()
        self.maze, self.edgeWeights = self.createMaze()

    def graph(self):
        x, y = self.width, self.height
        nodes, edges = set(), set()
        for w in range(x):
            for h in range(y):
                nodes.add((w, h))
                self.checkInBoundsGraph(w, h, edges, x, y)
        return nodes, edges

    def checkInBoundsGraph(self, currX, currY, edges, maxX, maxY):
        if currX < maxX - 1:
            edges.add(((currX, currY), (currX + 1, currY)))
        if currX > 0:
            edges.add(((currX, currY), (currX - 1, currY)))
        if currY < maxY - 1:
            edges.add(((currX, currY), (currX, currY + 1)))
        if currY > 0:
            edges.add(((currX, currY), (currX, currY - 1)))

    def generateRandomEdgeWeights(self):
        # random.seed(10)  # just for debugging purposes
        edgeWeights = [(random.randint(1, 100), x, y) for (x, y) in self.edges]
        return edgeWeights

    """ helper functions for Kruskals taken from https://www.programiz.com/dsa/kruskal-algorithm """

    def createMaze(self):
        edgeWeights = self.generateRandomEdgeWeights()
        rank = {n: 0 for n in self.nodes}
        parent = {n: n for n in self.nodes}
        resultArray = []
        result = set()

        for weight, x, y in sorted(edgeWeights):
            if x != y and self.find(parent, x) != self.find(parent, y):
                resultArray.append((weight, x, y))
                result.add((x, y))
                self.apply_union(parent, rank, x, y)

        return result, resultArray

    # https://www.programiz.com/dsa/kruskal-algorithm
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # https://www.programiz.com/dsa/kruskal-algorithm
    def apply_union(self, parent, rank, x, y):
        xRoot, yRoot = self.find(parent, x), self.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1
