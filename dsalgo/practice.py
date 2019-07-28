from collections import defaultdict

class PQ:
	"""We want a data structure which can
	1) given a node as a key return distance
	2) Give a node with minimum distance
	3) Allow us to update a distance
		We will find a node
		We will update distance
		We will rebalnace heap
	"""

	def __init__(self):
		self.heap = []
		self.dic = {} # Given a node return index in an array

	def add_nodes(self, pq):
		self._build_heap(pq)

	def _build_heap(self, pq):
		# I will pass PQ, array of (node, dist)
		# I want to update heap
		# I want to populate dictionary

		self.heap = pq
		for index,tt in enumerate(self.heap):
			self.dic[tt[0]] = index

		for index in range(len(self.heap) / 2 + 1, -1, -1):
			self._heapify(index)

	def _heapify(self, index):
		# Swap parent with smallest child if any smaller child exists
		child = index
		left, right = 2*index + 1, 2*index + 2
		if left < len(self.heap) and self.heap[left][1] < self.heap[child][1]:
			child = left
		if right < len(self.heap) and self.heap[right][1] < self.heap[child][1]:
			child = right
		if child != index:
			self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
			self.dic[self.heap[child][0]] = child
			self.dic[self.heap[index][0]] = index
			self._heapify(child)

	def _decrease_key(self, index, new_distance):
		# When we decrease distance we want this node to move up
		tt = self.heap[index]
		self.heap[index] = (tt[0], new_distance)
		parent = (index-1)/2
		while parent >= 0:
			if self.heap[parent][1] > self.heap[index][1]:
				self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
				self.dic[self.heap[parent][0]] = parent
				self.dic[self.heap[index][0]] = index
				index = parent
				parent = (index-1)/2
			else:
				break

	def get_distance(self, node):
		index = self.dic[node]
		return self.heap[index][1]

	def get_min(self):
		node, distance = self.heap[0]
		del self.dic[node]

		self.heap[0] = self.heap[-1]
		self.dic[self.heap[0][0]] = 0
		del self.heap[-1]
		self._heapify(0)

		return node, distance

	def update_distance(self, node, new_distance):
		index = self.dic[node]
		current_distance = self.heap[index][1]
		if new_distance < current_distance:
			self._decrease_key(index, new_distance)

	def empty(self):
		return len(self.heap) == 0


class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = set()

	def addEdge(self, u, v, w):
		self.graph[u].append((v,w))
		self.graph[v].append((u,w))
		self.vertices.update([u,v])

	def dijkstra(self, s):
		mypq = PQ()
		BIG_NO = 10 ** 8
		pq=[]
		for v in self.vertices:
			if v==s:
				pq.append((s,0))
			else:
				pq.append((v,BIG_NO))
		mypq.add_nodes(pq)

		def relax_edge(u,v,w):
			dist_u, dist_v = ans[u], mypq.get_distance(v)
			if dist_u + w < dist_v:
				dist_v = dist_u + w
				mypq.update_distance(v, dist_v)
				parent[v] = u

		parent = {s: None}

		ans = {}
		while not mypq.empty():
			node, dist = mypq.get_min()
			ans[node] = dist
			for neighbour, weight in self.graph[node]:
				if neighbour not in ans:
					relax_edge(node, neighbour, weight)

		return ans



if __name__ == '__main__':
	graph = Graph()  # It is a directed Graph
	graph.addEdge(1, 2, 4)
	graph.addEdge(1, 8, 8)
	graph.addEdge(2, 3, 8)
	graph.addEdge(2, 8, 11)
	graph.addEdge(3, 4, 7)
	graph.addEdge(3, 9, 2)
	graph.addEdge(3, 6, 4)
	graph.addEdge(4, 5, 9)
	graph.addEdge(4, 6, 14)
	graph.addEdge(5, 6, 10)
	graph.addEdge(6, 7, 2)
	graph.addEdge(7, 8, 1)
	graph.addEdge(7, 9, 6)
	graph.addEdge(8, 9, 7)
	print graph.graph
	ans = graph.dijkstra(1)
	for key in ans:
		print key, ans[key]




