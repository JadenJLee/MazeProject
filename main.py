from maze_main.maze_creator.generator import Generator
from maze_main.maze_visualizer.visualizer import Visualizer
from maze_main.maze_solver.solverDijkstra import DijkstraSolver

"""
This is the main file that calls all the functions.

Running python main.py creates two files under /MazeProject/pictures that is for the maze before the solution and after.
"""


class Main:
    def __init__(self, width, height):
        self.mazeSolver = None
        self.width = width
        self.height = height
        self.maze = Generator(self.width, self.height)  # create maze
        self.visualization = self.visualization()  # draw maze
        self.solve()  # solve maze
        self.visualization.saveAsImage()
        self.visualization.drawSolver()

    def visualization(self):
        vis = Visualizer(self.width, self.height, self.maze)
        return vis

    def solve(self):
        entryPt = self.visualization.entry
        exitPt = self.visualization.exit
        self.mazeSolver = DijkstraSolver(entry=entryPt, exit=exitPt)
        self.mazeSolver.fillGraph(self.maze.nodes, self.maze.edgeWeights)  # fill in graph from existing information
        self.mazeSolver.dijkstra()
        target = self.mazeSolver.graph.get_vertex(exitPt)
        path = [target.get_id()]
        self.mazeSolver.shortest(target, path)
        self.visualization.path = path[::-1]
        print(path[::-1])


Main(20, 20)
