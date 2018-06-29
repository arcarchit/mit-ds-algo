# Cycle is prsent if there is backward edge in DFS


from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.parent = {}
        self.stack = set()

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.graph[u] = v

    def dfs_visit(self, s):
        for v in self.graph[s]:
            if v in self.stack:
                return True
            if v not in self.parent:
                self.parent[v] = s
                self.stack.add(v)
                has_cycle = self.dfs_visit(v)
                if has_cycle:
                    return True
                self.stack.remove(v)
        return False

    def has_cycle(self):
        for v in self.vertices:
            if v not in self.parent:
                self.stack.add(v)
                has_cycle = self.dfs_visit(v)
                if has_cycle:
                    return True
                self.stack.remove(v)
        return False


def main():

    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'd')
    g.add_edge('b', 'e')
    g.add_edge('e', 'd')
    g.add_edge('d', 'b')
    g.add_edge('c', 'e')
    g.add_edge('c', 'f')

    has_cycle = g.has_cycle()
    print "Has Cycle ", has_cycle


if __name__=="__main__":
    main()