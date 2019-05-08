# Reverse
# pair
# problem
# Return
# count
# of
# pair(i, j)
# such
# that
# i < j and arr[i] > 2 * arr[j]
#
# [1, 2, 3, 3, 1]
# pairs
# are(3, 1) and (3, 1)
# return 2


class TreeNode:

	def __init__(self, val):
		self.val, self.rank = val, 1 # Storing rank allows lots of things
		self.left, self.right = None, None
		self.height, self.parent = 1, None # For AVL

	def __str__(self):
		# Simple way to debug it
		left = str(self.left) if self.left else "-"
		right = str(self.right) if self.right else "-"
		ans = "[%s*%s : %s, %s] " %(self.val, self.rank, left, right)
		return ans




class BST:
	"""
	Attributes to add for AVL
	self.parent
	self.height

	Methods to add for AVL
	get_height()
	update_height()
	rebalance()
	rotate_left()
	rotate_right()
	"""

	def __init__(self):
		self.root = None

	def get_count(self, val):
		# Return no of nodes > val
		if not self.root:
			return 0
		else:
			current = self.root
			ans = 0
			while current:
				if val < current.val:
					ans += 1
					ans += current.right.rank if current.right else 0
					current = current.left
				elif val == current.val:
					ans += current.right.rank if current.right else 0
					break
				else:
					current = current.right
			return ans



	def insert(self, val):
		# TODO : AVL for balancing
		if not self.root:
			self.root = TreeNode(val)
		else:
			current = self.root
			while True:
				current.rank += 1
				if val <= current.val:
					if current.left:
						current = current.left
					else:
						new_node = TreeNode(val)
						new_node.parent = current
						current.left = new_node
						break
				else:
					if current.right:
						current = current.right
					else:
						new_node = TreeNode(val)
						new_node.parent = current
						current.right = new_node
						break
			self.update_height(new_node)
			self.rebalance(new_node)


	def update_height(self, node):
		height = lambda node : node.height if node else 0
		while node:
			node.height = max(height(node.left), height(node.right)) + 1
			node = node.parent

	def rebalance(self, node):
		# TODO
		pass


	def __str__(self):
		return str(self.root)


def reverse_pairs(arr):
	# sol(i) = sol(i-1) + computation
	bst = BST()
	ans = 0
	for i in range(len(arr)):
		temp = bst.get_count(2 * arr[i])
		ans += temp
		bst.insert(arr[i])
	print str(bst)
	return ans

def test_get_count():
	arr = [1, 5, 3, 3, 2]
	bst = BST()
	for x in arr:
		bst.insert(x)
	print str(bst)
	print bst.get_count(2)


def main():
	arr = [1,5,3,3,2,1]
	ans = reverse_pairs(arr)

	print ans


if __name__=="__main__":
	main()


