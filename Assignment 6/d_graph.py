# Course: CS261 - Data Structures
# Author: Corey McFarland
# Assignment: 6.2
# Description: To implement a weighted, directed graph.


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Method to add vertex to graph.
        """

        vertex = [0]

        # Initialize empty graph
        if self.v_count == 0:
            self.adj_matrix.append(vertex)

        else:
            # Add new column to matrix
            for v in range(self.v_count):
                self.adj_matrix[v].append(0)

            # Add new row to matrix
            for n in range(self.v_count):
                vertex.append(0)

            self.adj_matrix.append(vertex)

        self.v_count += 1
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Method to add an edge between two current vertices.
        """

        # Check if vertices and weight are valid
        if src >= self.v_count or dst >= self.v_count or weight < 0 or src == dst:
            return

        # Add or update weight
        self.adj_matrix[src][dst] = weight

        return
        
    def remove_edge(self, src: int, dst: int) -> None:
        """
        Method to remove edge between to current vertices.
        """

        # Check if vertices and weight are valid
        if src >= self.v_count or src < 0 or dst >= self.v_count or dst < 0 or self.adj_matrix[src][dst] <= 0:
            return

        # Remove weight
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Method to return list of vertices in graph.
        """

        v_list = []

        for v in range(self.v_count):
            v_list.append(v)

        return v_list

    def get_edges(self) -> []:
        """
        Method to return list of edges in graph.
        """

        e_list = []

        for src in range(self.v_count):
            for dst in range(self.v_count):
                if self.adj_matrix[src][dst] > 0:
                    e_elm = (src, dst, self.adj_matrix[src][dst])
                    e_list.append(e_elm)

        return e_list

    def is_valid_path(self, path: []) -> bool:
        """
        Method to determine if the provided path is valid within the graph.
        """

        if len(path) <= 1:
            return True

        for p in range(1, len(path)):
            if self.adj_matrix[path[p - 1]][path[p]] > 0:
                continue

            else:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Method to create a list of vertices in a DFS.
        """

        v_dfs = []
        stack = []

        # Check if starting vertex exists
        if v_start >= self.v_count:
            return v_dfs

        # Add initial vertices to visit
        for d in range(self.v_count):
            if self.adj_matrix[v_start][d] > 0:
                stack.append(d)

        v_dfs.append(v_start)

        # Check if end has been reached, all nodes have been visited, or there are no more nodes to visit.
        while v_end not in v_dfs and len(v_dfs) < self.v_count and len(stack) > 0:

            # Visit first node of stack
            cur_v = stack[0]

            # If node already visited, remove and go to next node in stack.
            if cur_v in v_dfs:
                stack.remove(cur_v)
                continue

            # Add unvisited node to dfs
            v_dfs.append(cur_v)

            # Add successors to start of stack to iterate through
            for e in range(self.v_count - 1, -1, -1):
                if self.adj_matrix[cur_v][e] > 0:
                    if e in stack:
                        stack.remove(e)

                    stack.insert(0, e)

        return v_dfs

    def bfs(self, v_start, v_end=None) -> []:
        """
        Method to create a list of vertices via BFS
        """

        v_bfs = []
        stack = []

        # Check if starting vertex exists
        if v_start >= self.v_count:
            return v_bfs

        # Add initial vertices to visit
        for d in range(self.v_count):
            if self.adj_matrix[v_start][d] > 0:
                stack.append(d)

        v_bfs.append(v_start)

        # Check if end has been reached, all nodes have been visited, or there are no more nodes to visit.
        while v_end not in v_bfs and len(v_bfs) < self.v_count and len(stack) > 0:

            # Visit first node of stack
            cur_v = stack[0]

            # If node already visited, remove and go to next node in stack.
            if cur_v in v_bfs:
                stack.remove(cur_v)
                continue

            # Add unvisited node to dfs
            v_bfs.append(cur_v)

            # Add successors to end of stack to iterate through
            for e in range(self.v_count):
                if self.adj_matrix[cur_v][e] > 0:
                    if e in stack:
                        continue

                    stack.append(e)

        return v_bfs

    def has_cycle(self):
        """
        Method to determine if a graph has a cycle.
        """

        # Check for cycles at each vertex
        for v in range(self.v_count):

            cur_v = v
            v_cycle = []
            stack = []

            # Add initial vertices to visit
            for e in range(self.v_count):
                if self.adj_matrix[cur_v][e] > 0:
                    stack.append(cur_v)
                    stack.append(e)

            # Check if there are no more nodes to visit.
            while len(stack) > 0:

                # Visit first node of stack, update predecessor vertex
                prev_v = stack[0]
                stack.remove(prev_v)
                cur_v = stack[0]
                nd = [prev_v, cur_v]

                # Check if edge has already been used
                if nd in v_cycle:
                    stack.remove(cur_v)
                    continue

                # If node already visited, cycle found.
                for e in range(len(v_cycle)):
                    if nd[1] == v_cycle[e][1]:
                        break
                    if nd[1] == v_cycle[e][0]:
                        for f in range(len(v_cycle)):
                            if nd[1] == v_cycle[f][0]:
                                return True

                # Add to visited nodes
                v_cycle.append(nd)
                stack.remove(cur_v)

                # Find successors
                for e in range(self.v_count - 1, -1, -1):

                    # If edge exists
                    if self.adj_matrix[cur_v][e] > 0:

                        # Check if node to visit is already in stack
                        for f in range(1, len(stack), 2):
                            if f > len(stack):
                                break

                            # Remove pending visit to avoid duplication of same direction
                            if e == stack[f]:
                                del stack[f]
                                del stack[f-1]

                        # Add successor and current vertex to stack if not already in stack to be visited
                        stack.insert(0, e)
                        stack.insert(0, cur_v)

        # No cycle found
        return False

    def dijkstra(self, src: int) -> []:
        """
        Method to use Dijkstra's algorithm to find the shortest path from one vertex to all others in the graph
        """

        # Initialize variables
        d_list = []
        queue = []
        vd = [src, 0]
        queue.append(vd)

        # Make make of all vertices
        for map in range(self.v_count):
                d_list.append(float('inf'))

        # Dijkstra's Algorithm
        while len(queue) > 0:

            # If unvisited, update map
            if d_list[queue[0][0]] == float('inf'):
                d_list[queue[0][0]] = queue[0][1]

                # For each potential successor
                for e in range(self.v_count):

                    # If edge exists
                    if self.adj_matrix[queue[0][0]][e] > 0:

                        # Make weight be edge weight plus previous weights
                        nd = [e, self.adj_matrix[queue[0][0]][e] + queue[0][1]]

                        # Place into the queue in ascending order
                        for p in range(len(queue)):
                            if nd[1] < queue[p][1]:
                                queue.insert(p, nd)
                                continue

                        queue.append(nd)

            else:
                # If visited, remove from queue
                del queue[0]

        return d_list


if __name__ == '__main__':
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)
    #
    #
    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))
    #
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    #
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)


    print("\nPDF - dijkstra() example 1")
    print("--------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    g.remove_edge(4, 3)
    print('\n', g)
    for i in range(5):
        print(f'DIJKSTRA {i} {g.dijkstra(i)}')


