from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, s, parents, visited_order):
        for x in self.graph[s]:
            if x not in parents:
                parents[x] = s
                visited_order.append(x)
                self.dfs_util(x, parents, visited_order)

    def dfs_visit(self, s):
        parents = {s : None}
        visited_order = [s]
        self.dfs_util(s, parents, visited_order)
        return parents, visited_order


def main():

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print ("Following is Breadth First Traversal"
                      " (starting from vertex 2)")
    pp, vv = g.dfs_visit(2)
    print "parents ",pp, "visited order ", vv


if __name__=="__main__":
    main()