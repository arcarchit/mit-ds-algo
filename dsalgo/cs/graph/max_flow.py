from collections import deque

class Graph:

	def __init__(self, graph):
		self.graph = graph


	def greedy(self, s, t):
		"""
		Complexity
		O(max_flow * [V^2 + E + E])
		= O(max_flow * V^2)
		It is a greedy strategy and solution is not optimal
		Example is given at : http://theory.stanford.edu/~tim/w16/l/l1.pdf
		"""

		def BFS():
			parent = {s:None}
			frontier = [s]
			while frontier and t not in parent:
				new_frontier = []
				for x in frontier:
					for index,capacity in enumerate(self.graph[x]):
						if flow[x][index] < capacity and capacity > 0 and index not in parent : #Edge qualifies
							new_frontier.append(index)
							parent[index] = x
				frontier = new_frontier

			if not t in parent:
				return False, None
			else:
				edges = []
				child = t
				while child:
					pp = parent[child]
					if pp is not None:
						edges.append((pp, child))
					child = pp
				return True, edges

		flow = [[0 for _ in range(len(self.graph[0]))] for _ in range(len(self.graph))]
		max_flow = 0
		while True:
			path_exists, edges = BFS()
			if path_exists:
				delta = min([self.graph[i][j] - flow[i][j] for i, j in edges])
				max_flow += delta
				for i,j in edges:
					flow[i][j] += delta
				print flow, max_flow
			else:
				return max_flow


	def ford_fulkerson(self, source, sink):
		# Complexity O(max_flow * E) = O(max_flow * V^2)
		# Space complexity : O(V^2), good thing is we don't have to store seperate array for flow
		# Even in previous array we can stop using seperate flow array, becuase all we need is residues.

		def BFS():
			# Return if path exists and path
			# Complexity O(V^2)
			parent = {source:None}
			qq = deque()
			qq.append(source)
			while qq:
				popped = qq.popleft()
				for index, val in enumerate(self.graph[popped]):
					if index not in parent and val > 0:
						parent[index] = popped
						qq.append(index)
			if sink in parent:
				edges = []
				child = sink
				while child is not None:
					pp = parent[child]
					if pp is not None:
						edges.append((pp, child))
					child = pp
				return True, edges
			else:
				return False, None

		max_flow = 0
		BIG_NO = 10 ** 9
		while True:
			path_exits, edges = BFS() # O(V^2) or O(E)
			if path_exits:
				delta = min([self.graph[i][j] for i,j in edges]) # O(E)
				max_flow += delta
				for i,j in edges:
					self.graph[i][j] -= delta
					self.graph[j][i] += delta
			else:
				print self.graph
				return max_flow





def main():
	graph = [[0, 16, 13, 0, 0, 0],
			 [0, 0, 10, 12, 0, 0],
			 [0, 4, 0, 0, 14, 0],
			 [0, 0, 9, 0, 0, 20],
			 [0, 0, 0, 7, 0, 4],
			 [0, 0, 0, 0, 0, 0]]

	g = Graph(graph)

	source = 0;
	sink = 5

	max_flow = g.greedy(source, sink)
	print "Max flow with greedy algo ", max_flow
	max_flow = g.ford_fulkerson(source, sink)
	print "Max flow with greedy algo ", max_flow


if __name__=="__main__":
	main()