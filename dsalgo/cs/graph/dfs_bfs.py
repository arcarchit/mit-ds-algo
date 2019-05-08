from collections import defaultdict


class Graph:


    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def BFS(self, u):
        # In BFS, you can maintain level_dic, parent_dic and visited_order
        # Time Complexity : O(V + E) since this is adjancy list, for adjancy matrix it would be O(V^2)
        # Space complexity : O(V) maximum nodes in queue/frontier
        level = 0
        level_dic = {u:level}
        parent = {u:None}
        visited_order = [u]

        frontier = [u]
        while frontier:
            level += 1
            new_frontier = []
            for x in frontier:
                for n in self.graph[x]:
                    if n not in parent:
                        parent[n] = x
                        level_dic[n] = level
                        visited_order.append(n)
            frontier = new_frontier

        return visited_order, parent, level_dic


    def DFS(self, u):
        # At first it seems that in DFS parents assigned is not true, but it will get modified later on.
        # Time Complexity : O(V + E) since this is adjancy list, for adjancy matrix it would be O(V^2)
        # Space complexity : O(V) maximum nodes in queue/frontier
        level = 0
        level_dic = {u : level}
        parent = {u:None}
        visited_order = []
        visited_set = set()
        stack = [u]

        while stack:
            popped = stack.pop()
            if popped not in visited_set:
                visited_set.add(popped)
                visited_order.append(popped)
                for n in self.graph[popped]:
                    if n not in visited_set:
                        stack.append(n)
                        parent[n] = popped # Parent of n is keep getting updated
        return visited_order, parent


    def DFS_with_level(self, u):
        # In recursion it is easy to maintain level, via backtracking
        # In iterative version we need to pass it as tuple

        # Time Complexity : O(V + E) since this is adjancy list, for adjancy matrix it would be O(V^2)
        # Space complexity : O(V) maximum nodes in queue/frontier

        level_dic = {u:0}
        parent = {u:None}
        visited_order = []
        visited_set = set()
        stack = [(u,0)]

        while stack:
            pn, pl = stack.pop()
            if pn not in visited_set:
                visited_order.append(pn)
                visited_set.add(pn)
                for n in self.graph[pn]:
                    if n not in visited_set:
                        level_dic[n] = pl + 1
                        parent[n] = pn
                        stack.append((n, pl+1))
        return visited_order, parent, level_dic


    def DFS_recu(self, u):

        visited_order = []
        visited_set = set()
        parent = {u:None}
        def sub_sol(n, level):
            if n not in visited_set:
                visited_order.append((n, level))
                visited_set.add(n)
                for g in self.graph[n]:
                    if g not in visited_set:
                        parent[g] = n          # Here also parent will keep getting updated
                        sub_sol(g, level+1)

        sub_sol(u, 0)

        return visited_order, parent


if __name__=="__main__":

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print "DFS", g.DFS(2)
    print "DFS with level ",g.DFS_with_level(2)
    print "DFS recur ", g.DFS_recu(2)
    print "BFS", g.BFS(2)
