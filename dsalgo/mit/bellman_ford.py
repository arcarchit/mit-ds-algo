from collections import defaultdict
from sys import maxint


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.vertices.add(u)
        self.vertices.add(v)

    def bellman_ford(self, source):
        def relax(u, v, w):
            if ans[u] + w < ans[v]:
                ans[v] = ans[u] + w
                parent[v] = u

        ans = {source:0}
        parent = {source:None}

        for v in self.vertices:
            if v != source:
                ans[v] = maxint

        for i in range(len(self.vertices) - 1):
            for u in self.graph:
                for v, w in self.graph[u]:
                    relax(u, v, w)

        print "Node\tDistance\tParent"
        for key in sorted(ans.keys()):
            print key, "\t\t", ans[key], "\t\t\t", parent[key]


# https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/

def main():
    g = Graph()
    g.add_edge('A', 'B', -1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 3)
    g.add_edge('B', 'D', 2)
    g.add_edge('B', 'E', 2)
    g.add_edge('D', 'C', 5)
    g.add_edge('D', 'B', 1)
    g.add_edge('E', 'D', -3)

    g.bellman_ford('A')


if __name__ == "__main__":
    main()