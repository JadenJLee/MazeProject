import heapq

''' 
Modified code from:
https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
Dijkstras is a very common algorithm with graphs, and so it made more sense to take an existing solution
and modify it to fit my needs.

Very basic Dijkstras implementation so that it returns the shortest legal path between two vertices in a graph.

returns
    path - array of edges that give the shortest path by distance

'''


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = 999999
        self.visited = False
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def set_previous(self, current):
        self.previous = current


class DijkstraSolver:
    def __init__(self, entry, exit):
        self.graph = Graph()
        self.entry = entry
        self.exit = exit

    def shortest(self, v, path):
        if v.previous:
            path.append(v.previous.get_id())
            self.shortest(v.previous, path)
        return

    def get_weight(self, node):
        x1, y1 = node
        weights = [abs(x1 - self.exit[0]) + abs(y1 - self.exit[1])]
        weight = min(weights)
        return weight

    def fillGraph(self, nodes, weights):
        for n in nodes:
            self.graph.add_vertex(n)
        for weight, x, y in weights:
            self.graph.add_edge(x, y, weight)

    def dijkstra(self):
        print('''Dijkstra's shortest path''')
        start = self.graph.get_vertex(self.entry)
        start.set_distance(0)

        unvisited_queue = [(v.get_distance(), v) for v in self.graph]
        heapq.heapify(unvisited_queue)

        while len(unvisited_queue):
            uv = heapq.heappop(unvisited_queue)
            current = uv[1]
            current.set_visited()

            for next in current.adjacent:
                if next.visited:
                    continue
                new_dist = current.get_distance() + current.get_weight(next)

                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                else:
                    pass

            while len(unvisited_queue):
                heapq.heappop(unvisited_queue)
            unvisited_queue = [(v.get_distance(), v) for v in self.graph if not v.visited]
            heapq.heapify(unvisited_queue)
