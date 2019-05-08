from collections import deque

class Graph:

	def __init__(self, graph):
		self.graph = graph

	def bfs(self, s):
		"""
		Complexity : O(N^2), simple grid you know
		:param s:
		:return:
		"""
		q = deque()
		q.append(s)

		visited = set()
		ans = []
		while q:
			node = q.popleft()
			if node not in visited:
				visited.add(node)
				ans.append(node)
				neighbours = self.graph[node]
				for n, check in enumerate(neighbours):
					if check == 1 and n != node and n not in visited:
						q.append(n)

		return ans


	def dfs(self, s):
		"""
		Complexity again : O(N^2)
		:param s:
		:return:
		"""
		stack = [s]
		visited = set()
		ans = []

		while stack:
			node = stack.pop()
			if node not in visited:
				visited.add(node)
				ans.append(node)
				neighbours = self.graph[node]
				for n, check in enumerate(neighbours):
					if check == 1 and n != node and n not in visited:
						stack.append(n)

		return ans



def main():
	"""

	0 4 5 6
	4 0 3 2
	5 3 0 1
	6 2 1 0

	What if w(a,b) != w(b, a)
	Will dijkstra work. Above is same as directed graph where w(b,a) is infinity
	:return:
	"""

	arr = [
		[1,1,1,0],
		[1,1,1,0],
		[1,1,1,1],
		[0,0,1,1]
	]
	graph = Graph(arr)

	print "DFS", graph.dfs(2)
	print "BFS", graph.bfs(2)


if __name__=="__main__":
	main()


