from collections import defaultdict

"""
We are using adjancy list representation of graph
This is also directed graph
"""
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, node_a, node_b):
        self.graph[node_a].append(node_b)

    def BFS(self, start_node):

        queue = []
        visited = [False]*len(self.graph)


        queue.append(start_node)

        visited[start_node]=True

        while queue:
            popped_node = queue.pop(0)
            print popped_node
            neighbours = self.graph[popped_node]

            for node in neighbours:
                if not visited[node]:
                    visited[node]=True
                    queue.append(node)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)