
class TreeNode:
	def __init__(self, val):
		self.left, self.right = None, None
		self.val = val
		self.height = 1 # Root has height of 1
		self.parent = None

	def __str__(self, depth):
		ret = ""
		if self.right:
			ret += self.right.__str__(depth + 1)
		ret += "\n" + ("   "* depth) + str(self.val)
		if self.left:
			ret += self.left.__str__(depth + 1)
		return ret


class AVL:

	def __init__(self):
		self.root = None

	def insert(self, val):
		if not self.root:
			self.root = TreeNode(val)
		else:
			current = self.root
			new_node = None
			while not new_node:
				if val <= current.val:
					if current.left:
						current = current.left
					else:
						new_node = TreeNode(val)
						current.left = new_node
						new_node.parent = current
				else :
					if current.right:
						current = current.right
					else:
						new_node = TreeNode(val)
						current.right = new_node
						new_node.parent = current
			self._update_height(new_node)
			self._rebalance(new_node)

	def _update_height(self, node):
		height = lambda  x : x.height if x else 0
		while node:
			node.height = max(height(node.left), height(node.right)) + 1
			node = node.parent

	def _rebalance(self, node):
		ch = node
		p1 = node.parent
		p2 = p1.parent if p1 else None
		if not p2:
			return

		height = lambda x:x.height if x else 0

		lh, rh = height(p2.left), height(p2.right)

		if lh - rh >= 2: # lh has more height
			if p1.left:
				self._rotate_right(p2)
			elif p1.right:
				self._rotate_left(p1)
		elif rh - lh >= 2:
			if p1.right:
				self._rotate_left(p2)
			else:
				self._rotate_right(p1)
				self._rotate_left(p2)

	def _rotate_left(self, node):
		right, parent = node.right, node.parent

		# Settling node's parent
		right.parent = parent
		if parent:
			if parent.left == node:
				parent.left = right
			else:
				parent.right = right
			right.height = parent.height - 1
		else:
			right.height = 2
			self.root = right

		# Settling node
		node.parent = right
		right.left = node
		node.right = None

		node.height = right.height - 1

	def _rotate_right(self, node):
		left, parent = node.left, node.parent

		# Settling node's parent
		left.parent = parent
		if parent:
			if parent.left == node:
				parent.left = left
			else:
				parent.right = left
			left.height = parent.height - 1
		else:
			left.height = 2
			self.root = left

		# Settling node
		node.parent = left
		left.right = node
		node.left = None

		node.height = left.height - 1

	def level_order(self):
		frontier = [self.root]
		ans = []
		while frontier:
			new_frontier = []
			temp = []
			for n in frontier:
				temp.append(n.val)
				if n.left:
					new_frontier.append(n.left)
				if n.right:
					new_frontier.append(n.right)
			ans.append(temp)
			frontier = new_frontier
		return ans

	def print_tree(self):
		pass


def main():
	bst = AVL()
	bst.insert(1)
	bst.insert(2)
	bst.insert(3)
	bst.insert(4)
	bst.insert(5)
	bst.insert(6)
	bst.insert(7)
	print bst.level_order()
	print bst.root.__str__(0)
	bst = AVL()
	bst.insert(7)
	bst.insert(6)
	bst.insert(5)
	bst.insert(4)
	bst.insert(3)
	bst.insert(2)
	bst.insert(1)
	print bst.level_order()
	print bst.root.__str__(0)

if __name__=="__main__":
	main()