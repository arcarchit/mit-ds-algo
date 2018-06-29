from collections import defaultdict

"""
Adjency list representation of directed graph
"""
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def sub_dfs(self, node, visited):
        print node,
        visited[node] = True
        neighbours = self.graph[node]
        for n in neighbours:
            if not visited[n]:
                self.sub_dfs(n, visited)

    def DFS(self, start_node):
        visited = [False] * len(self.graph)
        self.sub_dfs(start_node, visited)

    def DFS_stack(self, start_node):
        visited = [False]*len(self.graph)
        stack = []
        stack.append(start_node)

        while stack:

            top = stack.pop(-1) # pop (-1) is equalt to pop(0)

            if visited[top]:
                continue
            else:
                print top,
                visited[top] = True
                for neighbour_node in self.graph[top]:
                        stack.append(neighbour_node)


# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is DFS from (starting from vertex 2)"
g.DFS(2)

print "Following is DFS from (starting from vertex 2)"
g.DFS_stack(2)