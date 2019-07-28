from collections import defaultdict


# For Undirected graph, cycle can be detected using Union Find, Complexity O(E logV) - Available at minimum_spanning_tree.py
# For directed graph we do DFS, complexity O(V + E)
# DFS works for undirected graph as well

# https://www.quora.com/How-do-I-detect-a-cycle-in-a-directed-graph

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
		self.vertices = set()

	def add_edge(self, u, v):
		self.graph[u].append(v)
		self.vertices.add(u)
		self.vertices.add(v)

	def check_cycle(self):
		# TODO : Check online, check cycle can not be done via iterative DFS, it has to be recursive

		visited_set = set()
		stack_set = set()

		def sub_sol(u):
			stack_set.add(u)
			if u not in visited_set:
				visited_set.add(u)
				for g in self.graph[u]:
					if g in stack_set:
						return True
					else:
						if g not in visited_set:
							sub = sub_sol(g)
							if sub:		# THIS is IMP, you always need to return once cycle if found, if not keep checking
								return True
			stack_set.remove(u)
			return False

		ans = False

		for v in self.vertices:
			if v not in visited_set:
				ans = sub_sol(v)
				if ans:
					break

		return ans


	def get_back_edges(self):
		# TODO : Check example on internet
		visited_set = set()
		stack_set = set()
		back_edges = []

		def sub_sol(u):
			stack_set.add(u)
			if u not in visited_set:
				visited_set.add(u)
				for g in self.graph[u]:
					if g in stack_set:
						back_edges.append((u, g))
						continue
					else:
						if g not in visited_set:
							sub_sol(g)
			stack_set.remove(u)

		for v in self.vertices:
			if v not in visited_set:
				sub_sol(v)

		return back_edges


def main():
	graph = Graph()
	graph.add_edge(1,2)
	graph.add_edge(2,3)
	graph.add_edge(3,4)
	graph.add_edge(4,5)
	graph.add_edge(5,3)
	graph.add_edge(5,2)
	graph.add_edge(1,3)

	print graph.check_cycle()
	print graph.get_back_edges()

if __name__=="__main__":
	main()