"""
https://www.geeksforgeeks.org/topological-sorting/
Possible only for DAG : Directed Acyclic Graph
"""

"""
Recusiton + Stack
Stack + Stack
Visite dlist is obviously there
"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topo_sub(self, stack, node):
        for neighbour in self.graph[node]:
            self.topo_sub(stack, neighbour)
        stack.append(node)

    def topologicalSort(self):
        # Two steps, build stack, print stack
        node = 2
        start_node = node
        stack = []
        self.topo_sub(stack, start_node)

        for i in reversed(stack):
            print i,


g = Graph()
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print "Following is a Topological Sort of the given graph"
g.topologicalSort()