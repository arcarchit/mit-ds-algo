from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):

        i = 0
        level = {s: 0}
        parent = {s: None}
        frontier = [s]
        visited_order = [s]

        while len(frontier) !=0:
            for v in frontier:
                next_frontier = []
                i = i + 1
                for x in self.graph[v]:
                    if x not in level:
                        next_frontier.append(x)
                        parent[x] = v
                        level[x] = i
                        visited_order.append(x)
            frontier = next_frontier

        return level, parent,visited_order


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
    ll, pp, vv = g.bfs(2)
    print "levels ",ll, "parents ",pp, "visited order ", vv


if __name__=="__main__":
    main()