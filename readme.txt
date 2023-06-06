Hello!
To run the code, run:
``` python main.py ```
in an IDE of choice. (Developed on PyCharm)

Requires pip install of basic python libraries if needed.

In the /src folder, you can find the main files under maze_main that are used for the application.
At the top of each class, there is a short description as well as what the class returns.

To break it down simply:
    generator.py - creates the maze
    visualizer.py - takes the graph and makes it look like a maze and prints out the images to the folder named output
    solverDijkstra.py - The algorithm to solve the maze, finding the optimal solution
    test.py - Unit tests for the mazes.

Why Kruskals Algorithm for building a maze?
- Finds a minimum spanning tree in a weighted, connected graph.
- Connected graph means that there is a path to each vertex to every other vertex (so maze is solvable!)
- No cycles which makes my life and coding a lot easier.

Why Dijkstra's Algorithm for solving a maze?
- I did it in school
- No but actually, it's a very nice algorithm for finding the shortest path between two nodes in a graph.
- It can return a variety of things. It can:
    - return distance between two nodes, distances between a node and all other nodes, distance and a path, distance and a previous node, etc.
- very powerful algorithm in the case of a maze because it solves it perfectly and most efficiently. (which is cool too).