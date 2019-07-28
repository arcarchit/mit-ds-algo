# It is also known as disjoint set

# Idea is to connect nodes
# Operations:
	# 1) Connect two nodes
	# 2) Return if two nodes are connected
	# 3) Return how many clusters are there
# Two main function :
	# 1) Union
	# 2) Find parrent
# Two optimization to stop growing linear tree
	# 1) Union by rank : smaller rank tree as child
	# 2) Path Compression in find : assign parent directly to grandchild

#COMPLEXITY ?
# Naive approach can have complexity of O(n)
# Just using rank bring down time complexity to O(log n)
# Using both rank and path compression makes it almost complex

# It allows to connect nodes, not to separate them
# I guetree, tree/linked list can help there
# CLRS had Union find via linked list


from collections import defaultdict

class UnionFind:

	def __init__(self, ll):
		self.ary = ll
		self.parent = [i for i in range(len(ll))]
		self.rank = [0 for _ in range(len(ll))] # Rank as height of the tree

	def union(self, i, j):
		parent_i = self.find_parent(i)
		parent_j = self.find_parent(j)

		rank_i, rank_j = self.rank[parent_i], self.rank[parent_j] ## UNION BY RANK HAS COMPLEXITY OF O(log N) same as union by size
		if rank_i < rank_j:
			self.parent[parent_i] = parent_j
		elif rank_j < rank_i:
			self.parent[parent_j] = parent_i
		else:
			self.parent[parent_j] = parent_i    ## We increment rank only if it is equal
			self.rank[parent_i] += 1




	def find_parent(self, i):
		x = i
		parent_i = self.parent[i]
		while parent_i != i:
			i = parent_i
			parent_i = self.parent[i]
		self.parent[x] = parent_i  ## PATH COMPRESSION
		return parent_i


	def check_connected(self, i, j):
		return self.find_parent[i] == self.find_parent[j]


	def get_no_clusters(self):
		dic = defaultdict(list)
		visited = set()
		for i in range(len(self.ary)):
			if i in visited:
				continue
			parent_i = self.parent[i]
			if parent_i == i:
				dic[i].append(i)
				visited.add(i)
			else:
				on_path = set()
				while parent_i != i:
					if i not in visited:
						on_path.add(i)
						visited.add(i)
					i = parent_i
					parent_i = self.parent[i]
				for x in on_path:
					dic[parent_i].append(x)
		return len(dic.keys())


def main():
	ll = [1,2,3,4,5,6,7]
	uf = UnionFind(ll)
	print uf.get_no_clusters()
	uf.union(1,4)
	print uf.get_no_clusters()
	uf.union(2, 6)
	uf.union(4, 2)
	uf.union(2, 0)
	uf.union(3, 5)
	print uf.parent
	print uf.get_no_clusters()


if __name__=="__main__":
	main()