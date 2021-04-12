# Course: CS261 - Data Structures
# Author: Corey McFarland
# Assignment: 6.1
# Description: To implement an Undirected Graph


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Method to add a vertex to graph.
        """

        if v in self.adj_list:
            return

        self.adj_list[v] = []

        return

    def add_edge(self, u: str, v: str) -> None:
        """
        Method to add a edge between two vertices.
        """

        # Check if vertices are the same
        if u == v:
            return

        # Check if vertices exit, add if not
        if u not in self.adj_list:
            self.add_vertex(u)

        if v not in self.adj_list:
            self.add_vertex(v)

        # Check if edge already exists
        if u in self.adj_list[v] or v in self.adj_list[u]:
            return

        # Add edge to both vertices and sort
        self.adj_list[u].append(v)
        self.adj_list[u].sort()
        self.adj_list[v].append(u)
        self.adj_list[v].sort()

        return

    def remove_edge(self, v: str, u: str) -> None:
        """
        Method to remove edge from two vertices.
        """

        # Check if vertices in edge are in list
        if u not in self.adj_list or v not in self.adj_list:
            return

        # Check if vertices are the same
        if u == v:
            return

        # Check if vertices are not connected
        if v not in self.adj_list[u] or u not in self.adj_list[v]:
            return

        # Remove edge from each vertex in matrix
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

        return

    def remove_vertex(self, v: str) -> None:
        """
        Method to remove vertex and any related edges.
        """

        # Check if vertex isn't in list
        if v not in self.adj_list:
            return

        for vert in self.adj_list:

            # Check other all vertices first
            if vert == v:
                continue

            # Check edges in each vertex and remove connections to the vertex to be removed.
            else:
                if v in self.adj_list[vert]:
                    self.adj_list[vert].remove(v)

        # Remove vertex from dictionary
        del self.adj_list[v]

        return

    def get_vertices(self) -> []:
        """
        Method to return list of the vertices in a graph.
        """

        vertex_list = []

        for v in self.adj_list:
            vertex_list.append(v)

        return vertex_list

    def get_edges(self) -> []:
        """
        Method to return list of the edges in a graph.
        """

        edge_list = []

        for v in self.adj_list:
            for e in self.adj_list[v]:

                # Check if edge is in correct order
                if e < v:
                    continue

                edge_t = (v, e)

                # If edge is already in list, skip
                if edge_t in edge_list:
                    continue

                # Else add to list
                else:
                    edge_list.append(edge_t)

        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Method to determine if provided path of vertices is valid.
        """

        # Check if path is empty
        if len(path) == 0:
            return True

        # Check if vertex of single vertex path exists
        if len(path) == 1:
            if path[0] in self.adj_list:
                return True
            else:
                return False

        edge_list = self.get_edges()

        # Iterate through path
        for e in range(1, len(path)):

            # Check if vertex exists
            if path[e - 1] not in self.adj_list:
                return False

            # Format edge
            if path[e - 1] < path[e]:
                edge_t = (path[e - 1], path[e])
            else:
                edge_t = (path[e], path[e - 1])

            # Check if edge exists and go to next edge if so
            if edge_t in edge_list:
                continue

            # If edge does not exist return false
            else:
                return False

        # All edges have been iterated through and exist, return true
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Method to create a list of vertices via DFS.
        """

        v_dfs = []
        stack = []

        # Check if starting vertex exists
        if v_start not in self.adj_list:
            return v_dfs

        # Add initial vertices to visit
        for se in self.adj_list[v_start]:
            stack.append(se)

        v_dfs.append(v_start)

        # Check if end has been reached, all nodes have been visited, or there are no more nodes to visit.
        while v_end not in v_dfs and len(v_dfs) < len(self.get_vertices()) and len(stack) > 0:

            # Visit first node of stack
            cur_v = stack[0]

            # If node already visited, remove and go to next node in stack.
            if cur_v in v_dfs:
                stack.remove(cur_v)
                continue

            # Add unvisited node to dfs
            v_dfs.append(cur_v)

            # Add successors to start of stack to iterate through
            for e in range(len(self.adj_list[cur_v]) - 1, -1, -1):
                if self.adj_list[cur_v][e] in stack:
                    stack.remove(self.adj_list[cur_v][e])

                stack.insert(0,self.adj_list[cur_v][e])

        return v_dfs

    def bfs(self, v_start, v_end=None) -> []:
        """
        Method to create a list of vertices via BFS
        """

        v_bfs = []
        stack = []

        # Check if starting vertex exists
        if v_start not in self.adj_list:
            return v_bfs

        # Add initial vertices to visit
        for se in self.adj_list[v_start]:
            stack.append(se)

        v_bfs.append(v_start)

        # Check if end has been reached, all nodes have been visited, or there are no more nodes to visit.
        while v_end not in v_bfs and len(v_bfs) < len(self.get_vertices()) and len(stack) > 0:

            # Visit first node of stack
            cur_v = stack[0]

            # If node already visited, remove and go to next node in stack.
            if cur_v in v_bfs:
                stack.remove(cur_v)
                continue

            # Add unvisited node to dfs
            v_bfs.append(cur_v)

            # Add successors to end of stack to iterate through
            for e in self.adj_list[cur_v]:
                if e in stack:
                    continue

                stack.append(e)

        return v_bfs

    def count_connected_components(self):
        """
        Method to return the number of connected components in the graph.
        """

        cc_list = []

        # For each vertex, run DFS, sort, then check if the component has been encountered.
        for v in self.get_vertices():
            cc_cmp = self.dfs(v)
            cc_cmp.sort()

            # If in component list, go to next component
            if cc_cmp in cc_list:
                continue

            # Add to component list
            cc_list.append(cc_cmp)

        return len(cc_list)

    def has_cycle(self):
        """
        Method to determine if a graph has a cycle
        """

        # Check for cycles at each vertex
        for v in self.adj_list:

            cur_v = v
            v_cycle = []
            stack = []

            # Add initial vertices to visit
            for se in self.adj_list[cur_v]:
                stack.append(cur_v)
                stack.append(se)

            v_cycle.append(cur_v)

            # Check if there are no more nodes to visit.
            while len(stack) > 0:

                # Visit first node of stack, update predecessor vertex
                prev_v = stack[0]
                stack.remove(prev_v)
                cur_v = stack[0]

                # If node already visited, cycle found.
                if cur_v in v_cycle:
                    return True

                # Add to visited nodes
                v_cycle.append(cur_v)
                stack.remove(cur_v)

                # Find successors
                for e in range(len(self.adj_list[cur_v]) - 1, -1, -1):
                    if self.adj_list[cur_v][e] == prev_v:
                        continue

                    # If successor will be visited again, cycle found
                    if self.adj_list[cur_v][e] in stack:
                        return True

                    # Add successor and current vertex to stack
                    stack.insert(0, self.adj_list[cur_v][e])
                    stack.insert(0, cur_v)

        # No cycle found
        return False
   


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
