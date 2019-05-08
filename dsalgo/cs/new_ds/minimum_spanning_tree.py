"""
What is minimum spanning Tree?
==  It can be computed for connected, undirected and weighted graph
==  Tree which connects all the nodes and sum of edges are minimum

Application
Network design : connecting your offices in different cities

Kruskal's algorithm is greedy and yet optimal.

COMPLEXITY ?
Sorting of Edge take O(E log E)
Union find takes O(log V) at most, we do it atmost E times in a loop, hence O(E log V)
total = O(E log E + E log V)

Values of E can be almost V^2
O(E log E) = O( E log V^2) = O ( 2 * E * log V) = O(E log V)

Hence time complexity is either O(E log E) or O(E log V)
"""

from collections import defaultdict




class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))


    def has_cycle(self, edges_so_far, new_edge):
        """
        We will use union find
        Iterate through all edges
            make union of vertices
            For a new edge if we find both vertice are in same set, it is cyclic
        :param edges:
        :return:
        """
        edges = []
        edges.extend(edges_so_far)
        edges.append(new_edge)
        dicc = {}
        def union(x, y):
            if x not in dicc:
                dicc[x] = x
            if y not in dicc:
                dicc[y] = y
            parent_x = find_parent(x)
            parent_y = find_parent(y)
            dicc[parent_x] = parent_y

        def find_parent(x_in):
            x = x_in
            if x not in dicc:
                dicc[x] = x
            parent_x = dicc[x]
            while parent_x != x:
                x = parent_x
                parent_x = dicc[x]
            dicc[x_in] = parent_x
            return parent_x

        for e in edges:
            x, y, _ = e
            parent_x = find_parent(x)
            parent_y = find_parent(y)
            if parent_x == parent_y:
                return True
            union(x, y)

        return False

    def get_mst(self):
        """
        Return List of (u, v, w)
        :return:
        """
        all_edges = []
        edges_added = set()

        for x in self.graph:
            neighbour_list = self.graph[x]
            for y, w in neighbour_list:
                edge1 = (x, y)
                edge2 = (y, x)
                if edge1 in edges_added or edge2 in edges_added:
                    continue
                edges_added.add((x, y))
                all_edges.append((x, y, w))

                all_edges = sorted(all_edges, key=lambda x:x[2])

        no_of_vertice = len(self.graph)
        mst_edges = []
        edge_count = no_of_vertice  # MST has edges = no_of_vertice - 1

        for e in all_edges:
            if self.has_cycle(mst_edges, e):
                pass
            else:
                mst_edges.append(e)
                if len(mst_edges) == edge_count:
                    break

        return mst_edges


def main():
    g = Graph()
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    mst_edges = g.get_mst()
    print "\nEdges in MST are : \n"
    print mst_edges


if __name__=="__main__":
    main()