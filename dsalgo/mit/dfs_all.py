from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.parent = {}
        self.visited_order = []

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u] = v

    def dfs_visit(self, s):
        for v in self.graph[s]:
            if v not in self.parent:
                self.visited_order.append(v)
                self.parent[v] = s
                self.dfs_visit(v)

    def dfs_all(self):
        self.visited_order = []
        self.parent = {}
        for v in self.vertices:
            if v not in self.parent:
                self.parent[v] = None
                self.visited_order.append(v)
                self.dfs_visit(v)
        return self.visited_order


def main():

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'd')
    g.add_edge('d', 'b')
    g.add_edge('c', 'e')
    g.add_edge('c', 'f')

    ll = g.dfs_all()
    print "visited order ", ll


if __name__=="__main__":
    main()