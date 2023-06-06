from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

"""
This class is for displaying my maze and solution. 

returns:
    Figure/axes - from matplotlib, the actual drawing of the maze and the solution.
    Graph - as a dictionary of edges.
    Entry and exit points - where the maze starts and ends, 
        right now coded to be the bottom left for start and top right for end
    Path  - for optimal solution from start to the end. 
"""


class Visualizer:
    def __init__(self, width, height, maze):
        self.width = width
        self.height = height
        self.maze = maze
        self.edges = self.maze.maze
        self.figure, self.axes = self.plot()
        self.graph = defaultdict(list)
        self.entry, self.exit, self.entryExitEdges = self.entryExit()
        self.drawWalls()
        self.path = None

    def saveAsImage(self):
        plt.savefig("output/maze.png")

    def plot(self):
        figure = plt.figure()
        axes = plt.axes()
        return figure, axes

        """ debugging stuff I used, if this was production code, I would have deleted """
        # G = nx.Graph()
        # G.add_nodes_from(self.maze.nodes)
        # G.add_edges_from(self.maze.maze)
        # print(G.nodes)
        # print(G.edges)
        # pos = nx.spring_layout(G)
        # nx.draw_networkx(G, pos=pos, with_labels=True, node_size=15)
        # plt.show()

    """ 
    The following dfs function and helper functions were taken from 
    https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    """

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfsHelper(self, node, visited, data):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.wallDataHelper(node, neighbor, data)
                #  recursive step
                self.dfsHelper(neighbor, visited, data)

    def wallDataHelper(self, node, neighbor, data):
        # add wall to do not add list
        if node[0] == neighbor[0]:
            if node[1] > neighbor[1]:
                data.append([(node[1], node[1]), (node[0] + 1, node[0])])
            else:
                data.append([(node[1] + 1, node[1] + 1), (node[0], node[0] + 1)])
        if node[1] == neighbor[1]:
            if node[0] > neighbor[0]:
                data.append([(node[1], node[1] + 1), (node[0], node[0])])
            else:
                data.append([(node[1] + 1, node[1]), (node[0] + 1, node[0] + 1)])

    def drawWalls(self):
        visited = set()
        data = []
        temp = (0, 0)
        for e1, e2 in self.edges:
            self.addEdge(e1, e2)
            self.addEdge(e2, e1)  # because it is undirected graph, needs both ways
        self.dfsHelper(temp, visited, data)
        data.extend(self.entryExitEdges)

        for y in range(self.height):
            for x in range(self.width):
                top = [(x, x + 1), (y, y)]
                topv2 = [(x + 1, x), (y, y)]
                self.checkDontDraw(top, topv2, data)

                bot = [(x + 1, x), (y + 1, y + 1)]
                botv2 = [(x, x + 1), (y + 1, y + 1)]
                self.checkDontDraw(bot, botv2, data)

                right = [(x + 1, x + 1), (y, y + 1)]
                rightv2 = [(x + 1, x + 1), (y + 1, y)]
                self.checkDontDraw(right, rightv2, data)

                left = [(x, x), (y + 1, y)]
                leftv2 = [(x, x), (y, y + 1)]
                self.checkDontDraw(left, leftv2, data)

    def checkDontDraw(self, edge, edgev2, dontDraw):
        if edge not in dontDraw and edgev2 not in dontDraw:
            self.axes.plot(edge[0], edge[1], color="black", linewidth=3)

    def entryExit(self):
        data = []
        entryPt = (0, 0)  # entrance at the bottom left of the maze
        exitPt = (self.height - 1, self.height - 1)  # exit at the top right of the maze
        data.append([(entryPt[1], entryPt[1] + 1), (entryPt[0], entryPt[0])])
        data.append([(exitPt[1], exitPt[1] + 1), (exitPt[0] + 1, exitPt[0] + 1)])

        ### This code section for images was taken from stack overflow.
        ### https: // stackoverflow.com / questions / 65387500 / insert - a - png - image - in -a - matplotlib - figure
        img = plt.imread("src/images/end.png")
        imgstart = plt.imread("src/images/start.png")
        im = OffsetImage(imgstart, zoom=0.05)
        ab = AnnotationBbox(im, (0.1, -0.07), xycoords='axes fraction', box_alignment=(1.1, -0.1))
        self.axes.add_artist(ab)

        im2 = OffsetImage(img, zoom=0.02)
        ab2 = AnnotationBbox(im2, (1, 1), xycoords='axes fraction', box_alignment=(1.1, -0.1))
        self.axes.add_artist(ab2)

        entryRec = plt.Rectangle((entryPt[1], entryPt[0]), 1, 1, fc="green", alpha=1.0)
        self.axes.add_patch(entryRec)
        exitRec = plt.Rectangle((exitPt[1], exitPt[0]), 1, 1, fc="red", alpha=1.0)
        self.axes.add_patch(exitRec)

        return entryPt, exitPt, data

    def drawSolver(self):
        for t in self.path:
            rec = plt.Rectangle(t[::-1], 1, 1, fc="pink", alpha=1.0)
            self.axes.add_patch(rec)
        plt.savefig("output/solutionMaze.png")
