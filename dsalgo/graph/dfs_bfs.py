from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_sub(self, n, visited):
        print n,
        visited[n] = True
        for neighbour in self.graph[n]:
            if not visited[neighbour]:
                self.dfs_sub(neighbour, visited)

    def dfs_recursion(self, n):
        no_of_nodes = len(self.graph)
        visited = [False] * no_of_nodes
        self.dfs_sub(n, visited)

    def dfs(self,n):
        stack = []
        stack.append(n)

        no_of_nodes = len(self.graph)
        visited = [False]*no_of_nodes

        while len(stack) != 0:
            pop = stack.pop()
            print pop,
            visited[pop] = True
            for neighbour in self.graph[pop]:
                if not visited[neighbour]:
                    stack.append(neighbour)

    def bfs(self, n):
        queue = []
        queue.append(n)
        no_of_nodes = len(self.graph)
        visited = [False]*no_of_nodes
        while len(queue) != 0:
            pop = queue.pop()
            print pop,
            visited[pop] = True
            for neighbour in self.graph[pop]:
                if not visited[neighbour]:
                    queue.insert(0, neighbour)




g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is BFS from vertex 2"
g.bfs(2)

print "Following is DFS from (starting from vertex 2)"
g.dfs(2)

print "Following is DFS from (starting from vertex 2)"
g.dfs_recursion(2)