# Single Source, all targets
# Complexity O(V log V + E log V)
# O(V log V + E) can be achieved when we learn fibonacci heap data structure

# Can be applied to directed and non-directed graph
# Gravity demo works for directed graph
# Negative edges are not allowed
# Cycles are allowed (Does not cause any problem as negative edges are not allowed, there won't be any negative cycle)

# Idea
#   - EXTRACT_MIN is the key
#   - We get vertices in order of the distance from source

from collections import defaultdict
from sys import maxint


class PQ:

    def __init__(self):
        self.hp = []   # Array of tuples (key, name)
        self.dicc = {}

    def min_heapify(self, i):
        # 0, 1, 2, 3, 4, 5, 6, 7
        # left = 2*i + 1, right = 2*i + 2
        left, right = 2*i + 1, 2*i + 2
        smallest = i

        if left < len(self.hp)  and self.hp[i] > self.hp[left]:
            smallest = left

        if right < len(self.hp)  and self.hp[smallest] > self.hp[right]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def insert(self, name, key):
        new_tt = (key, name)
        self.hp.append(new_tt)
        self.dicc[name] = len(self.hp)-1
        self.decrease_key(name, key)

    def min(self):
        tt = self.hp[0]
        return tt[1], tt[0] # We always return name, key

    def dist(self, name):
        pos = self.dicc[name]
        tt = self.hp[pos]
        return tt[0]

    def swap(self, i ,j):
        tt_i = self.hp[i]
        tt_j = self.hp[j]
        self.dicc[tt_i[1]] = j
        self.dicc[tt_j[1]] = i

        self.hp[j], self.hp[i] = self.hp[i], self.hp[j]

    def decrease_key(self, name, new_key):
        i = self.dicc[name]
        current_val = self.hp[i]
        if new_key > current_val:
            raise Exception("New value is larger than current value")
        self.hp[i] = (new_key, name)
        while i != 0:
            # 0, 1, 2, 3, 4, 5
            # parent = (i - 1)/2
            parent = (i - 1)/2
            if self.hp[parent] > self.hp[i]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def extract_min(self):
        if len(self.hp)==1:
            val = self.hp.pop(-1)
            return val[1], val[0]
        else:
            val = self.hp[0]
            last = self.hp.pop(-1)
            self.hp[0] = last
            self.dicc[last[1]] = 0
            self.min_heapify(0)
            del self.dicc[val[1]]
            return val[1], val[0] # While giving back name should be first

    def is_empty(self):
        return len(self.hp) == 0


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.pq = PQ()

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w)) # Graph is undirected
        self.vertices.add(u)
        self.vertices.add(v)

    def dijkstra(self, source):
        parent = {}
        ans = {}
        parent[source] = None

        def relax(u, v, w):
            uu = ans[u]
            vv = pq.dist(v)
            if uu + w < vv:
                pq.decrease_key(v, uu + w)
                parent[v] = u

        pq = PQ()
        pq.insert(source, 0)
        for v in self.vertices:
            if v != source:
              pq.insert(v, maxint)

        while not pq.is_empty():
            tt_u = pq.extract_min()
            ans[tt_u[0]] = tt_u[1]
            for v, dist in self.graph[tt_u[0]]:
                if (v not in ans):
                    relax(tt_u[0], v, dist)

        print "Node\tDistance\tParent"
        for key in sorted(ans.keys()):
            print key, "\t\t", ans[key], "\t\t\t", parent[key]




def main():
    graph = Graph()  # It is a directed Graph
    graph.addEdge('A', 'B', 4)
    graph.addEdge('A', 'H', 8)
    graph.addEdge('B', 'C', 8)
    graph.addEdge('B', 'H', 11)
    graph.addEdge('C', 'D', 7)
    graph.addEdge('C', 'I', 2)
    graph.addEdge('C', 'F', 4)
    graph.addEdge('D', 'E', 9)
    graph.addEdge('D', 'F', 14)
    graph.addEdge('E', 'F', 10)
    graph.addEdge('F', 'G', 2)
    graph.addEdge('G', 'H', 1)
    graph.addEdge('G', 'I', 6)
    graph.addEdge('H', 'I', 7)
    graph.dijkstra('A')


"""
Expected ans : 

Vertex   Distance from Source
0                0
1                4
2                12
3                19
4                21
5                11
6                9
7                8
8                14
"""

if __name__ == "__main__":
    main()


