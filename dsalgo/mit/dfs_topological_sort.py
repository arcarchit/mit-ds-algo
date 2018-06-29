# Finishing time of vertices

from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.topological_list = []
        self.vertices = []
        self.parent = {}

    def addEdge(self, u, v):
        self.vertices.append(u)
        self.vertices.append(v)
        self.graph[u].append(v)

    def dfs_visit(self, s):
        for v in self.graph[s]:
            if v not in self.parent:
                self.parent[v] = s
                self.dfs_visit(v)
                self.topological_list.append(v)

    def topological_sort(self):
        for v in self.vertices:
            if v not in self.parent:
                self.parent[v] = None
                self.dfs_visit(v)
                self.topological_list.append(v)
        return list(reversed(self.topological_list))


def main():
    g = Graph()
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    ll = g.topological_sort()
    print "Topological sort ", ll


if __name__ == "__main__":
    main()
