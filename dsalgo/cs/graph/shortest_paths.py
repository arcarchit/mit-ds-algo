#https: // www.geeksforgeeks.org / top - algorithms - and -data - structures -for -competitive - programming /

#Graph

# Dijkstra
# Bellman Ford
#Floyd Warshall - works with negative edges
# not with negative cycles
# However ir can be used to detect negative cycle, in that cae one of the diagonal elements will be non zero



from collections import defaultdict


class MinimalPQ:

	def __init__(self):
		self.hp = [] # Stores tuples (dist, node)
		self.dic = {} # Given node return index in hpss

	def update_distance(self, node, new_dist):
		index = self.dic[node]
		self.hp[index][0] = new_dist
		self._decrease_key(index, new_dist)

	def _decrease_key(self, child, new_dist):
		if new_dist > self.hp[child][0]:
			raise Exception("New distance is smaller")

		parent = (child - 1)/2
		while parent > -1 and self.hp[parent] > self.hp[child]:
			self.swap(parent, child)
			child = parent
			parent = (child -1)/2

	def swap(self, i, j):
		self.hp[i], self.hp[j] = self.hp[j], self.hp[i]
		self.dic[self.hp[j][1]] = j
		self.dic[self.hp[i][1]] = i

	def insert(self, node, dist):
		tt = [dist, node]
		self.hp.append(tt)
		self.dic[node] = len(self.hp) - 1
		self._decrease_key(len(self.hp)-1, dist)


	def empty(self):
		return True if not self.hp else False

	def extract_min(self):
		if self.empty():
			raise Exception("PQ is empty")
		dist, node = self.hp[0]
		self.hp[0] = self.hp[-1]
		del self.hp[-1]
		self.heapify(0)
		return node, dist

	def heapify(self, parent):
		left, right = 2*parent+1, 2*parent+2
		child = parent
		if left < len(self.hp) and self.hp[left] < self.hp[child]:
			child = left
		if right < len(self.hp) and self.hp[right] < self.hp[child]:
			child = right
		if parent != child :
			self.swap(parent, child)
			self.heapify(child)

	def get(self, node):
		location = self.dic[node]
		print node, location, self.hp
		dist, node = self.hp[location]
		# TODO
		return node, dist



class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = set()

	def addEdge(self, u, v, d):
		self.graph[u].append((v, d))
		self.vertices.update([u, v])

	def dijkstra(self, s):
		# Complexity : O(E log V)
		BIG_NO = 1e10
		pq = MinimalPQ()
		for v in self.vertices:
			if v==s:
				pq.insert(v, 0)
			else:
				pq.insert(v, BIG_NO)

		ans = {}
		while not pq.empty():
			node, dist = pq.extract_min()
			ans[node] = dist
			print ans
			# Relax edge
			for nei, w in self.graph[node]:
				if nei not in ans:
					if pq.empty():
						break
					node, current_dist = pq.get(nei)
					proposed_dist = dist + w
					if proposed_dist < current_dist:
						pq.update_distance(nei, proposed_dist)
		return ans


	def floyd_warshall(self):
		# Complexity : O(V^3)
		# We keep adding k vertices one by one
		ans = [[1e10 for _ in self.vertices] for _ in self.vertices]
		parent = [[None for _ in self.vertices] for _ in self.vertices]

		for u in self.vertices:
			ans[u][u] = 0


		for u in self.vertices:
			for v, d in self.graph[u]:
				ans[u][v] = d
				parent[u][v] = (u,u)

		for k in self.vertices:
			for u in self.vertices:
				for v in self.vertices:
					current_distance = ans[u][v]
					propsed_distance = ans[u][k] + ans[k][v]
					if propsed_distance < current_distance:
						ans[u][v] = propsed_distance
						parent[u][v] = (u, k)

		return {
			'ans':ans,
			'parent':parent
		}

	def bellman_ford(self, source):
		# Time complexity : O(V*E)
		# Which becomes O(V^3) when graph is dense

		def relax(u, v, w):
			if ans[u] + w < ans[v]:
				ans[v] = ans[u] + w
				parent[v] = u

		ans = {source: 0}
		parent = {source: None}
		BIG_NO = 1e10
		for v in self.vertices:
			if v != source:
				ans[v] = BIG_NO

		for i in range(len(self.vertices) - 1):
			for u in self.graph:
				for v, w in self.graph[u]:
					relax(u, v, w)

		# Do one more pass to report negative cycle
		for u in self.graph:
			for v, w, in self.graph[u]:
				if ans[u] + w < ans[v]:
					raise Exception("There is negative cycle")

		print "Node\tDistance\tParent"
		for key in sorted(ans.keys()):
			print key, "\t\t", ans[key], "\t\t\t", parent[key]


def main():
	# graph = Graph()
	# graph.addEdge(0, 1, 5)
	# graph.addEdge(1, 2, 3)
	# graph.addEdge(2, 3, 1)
	# graph.addEdge(0, 3, 10)
	# dic = graph.floyd_warshall()
	# print dic['ans']
	# print dic['parent']
	#
	# graph = Graph()  # It is a directed Graph
	# graph.addEdge(1, 2, 4)
	# graph.addEdge(1, 8, 8)
	# graph.addEdge(2, 3, 8)
	# graph.addEdge(2, 8, 11)
	# graph.addEdge(3, 4, 7)
	# graph.addEdge(3, 9, 2)
	# graph.addEdge(3, 6, 4)
	# graph.addEdge(4, 5, 9)
	# graph.addEdge(4, 6, 14)
	# graph.addEdge(5, 6, 10)
	# graph.addEdge(6, 7, 2)
	# graph.addEdge(7, 8, 1)
	# graph.addEdge(7, 9, 6)
	# graph.addEdge(8, 9, 7)
	# print graph.graph
	# ans = graph.dijkstra(1)
	#
	# print ans

	g = Graph()
	g.addEdge('A', 'B', -1)
	g.addEdge('A', 'C', 4)
	g.addEdge('B', 'C', 3)
	g.addEdge('B', 'D', 2)
	g.addEdge('B', 'E', 2)
	g.addEdge('D', 'C', 5)
	g.addEdge('D', 'B', 1)
	g.addEdge('E', 'D', -3)

	g.bellman_ford('A')


if __name__=="__main__":
	main()





