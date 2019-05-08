from collections import defaultdict
import heapq

# Graph requirements : Weighted, connected, undirected

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = set()

	def vertices_count(self):
		return len(self.vertices)

	def add_edge(self, u, v, d):
		self.graph[u].append((v, d))
		self.graph[v].append((u, d))
		self.vertices.update([u, v])


	def prim_mst(self):
		# This code needs refinement, they are doing it via decrease_key, heap should not grow beyond |v|
		# Complexity : O(V log V + E log V) = O(E log V)
		# Using fibonaaci heap : O(E + log V)
		# TODO
		pass


	def kruskal_mst(self):
		# We want to return list of edges
		# Time complexity : O(E log E + E log V) = O(E log E) = O(E log V)
		# Greedy algorithm

		edges_set = set()
		edges_list = []

		# Get list of edges
		for u in self.graph.keys():
			for v, d in self.graph[u]:
				if (u, v) not in edges_set:
					edges_set.update([(u, v), (v, u)])
					edges_list.append((d, u, v))
		edges_list.sort()

		uf = UnionFind(list(self.vertices))
		edges_taken = []
		for d, u, v in edges_list:
			if not uf.is_connected(u, v):
				uf.union(u, v)
				edges_taken.append((u, v, d))
				if len(edges_taken) == len(self.vertices) - 1:
					break
		return edges_taken


class UnionFind:

	def __init__(self, ll):
		self.parent = [i for i in range(len(ll))]
		self.rank = [0 for _ in range(len(ll))]

	def union(self, u, v):
		parent_u, parent_v = self.find_parent(u), self.find_parent(v)
		rank_u, rank_v = self.rank[u], self.rank[v]

		if rank_u < rank_v:
			self.parent[parent_u] = parent_v
		elif rank_v < rank_u:
			self.parent[parent_v] = parent_u
		else:
			self.parent[parent_v] = parent_u
			self.rank[parent_u] += 1


	def find_parent(self, u):
		x = u
		parent_u = self.parent[u]
		while parent_u != u:
			u = parent_u
			parent_u = self.parent[u]
		self.parent[x] = parent_u # PATH COMPRESSION
		return parent_u


	def is_connected(self, u, v):
		return self.find_parent(u) == self.find_parent(v)




def main():
    g = Graph()
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst_edges = g.kruskal_mst()
    print "\nEdges in MST are : "
    print mst_edges

    print "\nPrim MST"
    print g.prim_mst()



if __name__=="__main__":
    main()
