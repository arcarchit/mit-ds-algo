# Q: After a rainstorm, water travels from the root of a tree to the leaves,
# moving at a constant rate of speed. If a tree is made up of a number of
# fixed-length “branch segments” arranged in a tree data structure, write a
# function that tells which leaf will get water first for a given tree.

class TreeNode:
	def __init__(self):
		self.children = []


def get_leaf(root):
	"""
	Return leaf which gets water first and time to rach water.
	We will return (node, time_taken) as tuple
	Complexity : O(height of the tree)
	:param root:
	:return:
	"""

	if not root:
		return (None, -1)

	frontier = [root]
	level = -1
	while frontier:
		new_frontier = []
		level += 1
		for x in frontier:
			if x.children:
				for n in x.children:
					new_frontier.append(n)
			else:
				return (x, level)
		frontier = new_frontier


# Q: Solve the same question, but the branch segments each have their own
# variable (non-integer) length.


class TreeNode:
	def __init__(self, dist_from_parent):
		self.children = []
		self.dist_from_parent = dist_from_parent # Root also has this value, time taken to suck up water


def get_leaf(root):
	"""
	Here also we want to return (node, height)
	Complexity : O(no of edges)
	:param root:
	:return:
	"""

	if not root:
		return (None, -1)

	BIG_NO = 10**8
	ans_so_far = (None, BIG_NO)

	def sub_sol(node, prev_dist):
		"""
		prev_distance does not include nodes's distance.
		I had started with Augementing distance from root, but I can do it just by passing prev_distance
		# Learning
		"""
		node_dist = prev_dist + node.dist_from_parent
		global ans_so_far
		if not node.children:
			if node_dist < ans_so_far[0]:
				ans_so_far = (node, prev_dist + node.dist_from_parent)
		else:
			for n in node.children:
				sub_sol(n, node_dist)

	sub_sol(root, 0)


# Q: What if we wanted to return all the leaves in the order they get water
# Also above is DFS, can you also do it via BFS

def get_all_nodes(root):
	"""
	We need to store them all and then sort
	Complexity O(N log N)
	We can not improve this complexity. Because if we can do it, we can sort anything using such trees.
	# TODO : Above needs to be realized

	Complexity : O(no of edges)
	:return:
	"""

	ans = []

	if not root:
		return ans

	def sub_sol(node, prev_dist):
		"""
		prev_distance does not include node
		:param node:
		:param prev_dist:
		:return:
		"""
		node_dist = prev_dist + node.dist_from_parent
		if not node.children:
			ans.append(node, node_dist)
		else:
			for n in node.children:
				sub_sol(n, node_dist)
	return ans

	ans = sub_sol(root, 0)
	ans.sort(key = lambda x:x[1])
	return ans


def get_all_nodes_bfs(root):
	ans = []
	if not root:
		return ans

	frontier = [(root, root.dist_from_parent)]
	while frontier:
		new_frontier = []
		for x in frontier:
			if x[0].children:
				for n in x[0].children:
					new_frontier.append((n, x[1]+n.dist_from_parent))
			else:
				ans.append(x)

		frontier = new_frontier

	return ans


