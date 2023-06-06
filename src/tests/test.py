import unittest
from maze_main.maze_creator.generator import Generator
from maze_main.maze_solver.solverDijkstra import DijkstraSolver


class TestMaze(unittest.TestCase):

    def test_check_width_height_of_maze(self):
        maze = Generator(20, 20)
        self.assertEqual(maze.width, 20)
        self.assertEqual(maze.height, 20)

    def test_number_of_nodes_is_correct(self):
        maze = Generator(5, 5)
        self.assertEqual(len(maze.nodes), 25)

    def test_number_of_edges_is_correct(self):
        maze = Generator(5, 5)
        self.assertEqual(len(maze.edges), 80)

    def test_exit_and_entrance_correct(self):
        vis = DijkstraSolver((0,0), (5,5))
        self.assertEqual(vis.exit, (5, 5))
        self.assertEqual(vis.entry, (0, 0))

    def test_number_of_verticies_solution_before_and_after(self):
        maze = Generator(20, 20)
        vis = DijkstraSolver((0, 0), (5, 5))
        self.assertEqual(vis.graph.num_vertices, 0)
        vis.fillGraph(maze.nodes, maze.edgeWeights)
        vis.dijkstra()
        self.assertEqual(vis.graph.num_vertices, 400)

