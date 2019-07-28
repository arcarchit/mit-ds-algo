"""
https://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/
https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


Therefore, following combination can uniquely identify a tree.
	Inorder and Preorder.
	Inorder and Postorder.
	Inorder and Level-order.

And following do not.
	Postorder and Preorder.
	Preorder and Level-order.
	Postorder and Level-order.

Definitions

Complete Binary Tree :
All the levels are filled up. Last level is filled as left as possible.
We can construct such a tree from level order traversal.
Like heap left and right child are at index 2i+1 and 2i+2.


Full Binary Tree :
Every node has 0 or two children.


"""

class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

def in_order(root):
	# Complexity O(N)
	# 2 1 4 3 5
	current = root
	ans = []
	st = []
	while current or st:
		if current:
			st.append(current)
			current = current.left
		else:
			popped = st.pop()
			ans.append(popped.val)
			current = popped.right
	return ans


def pre_order(root):
	# Complexity O(N)
	ans = []
	current = root
	st = []
	while current or st:
		if current :
			ans.append(current.val)
			if current.right:
				st.append(current.right)
			current = current.left
		else:
			current = st.pop()
	return ans


def post_order(root):
	# Complexity O(N)
	ans_st = []
	st = []
	current = root
	while current or st:
		if current:
			ans_st.append(current.val)
			if current.left:
				st.append(current.left)
			current = current.right
		else:
			current = st.pop()
	ans = ans_st[::-1]
	return ans


def construct_in_pre(in_oo, pre_oo):
	# Complexity O(N)

	dic = {} # Stores val to index mapping in of in_oo
	for index, val in enumerate(in_oo): dic[val] = index


	def sub_sol(in_start, in_end):

		if in_start > in_end:
			return None

		partition_val = pre_oo[index[0]]
		index[0] += 1

		index_ii = dic[partition_val]
		ans = TreeNode(partition_val)
		if in_start == in_end:
			return ans

		ans.left = sub_sol(in_start, index_ii-1)
		ans.right = sub_sol(index_ii+1, in_end)
		return ans

	index = [0]
	ans = sub_sol(0, len(pre_oo)-1)
	return ans


def construct_in_post(in_oo, post_oo):
	# Complexity : O(N)

	dic = {}
	for index, val in enumerate(in_oo):dic[val]=index

	def sub_sol(start, end):
		if start > end :
			return None

		val = post_oo[post_index[0]]
		post_index[0] -= 1


		ans = TreeNode(val)
		if start == end:
			return ans

		index_io = dic[val]
		ans.right = sub_sol(index_io + 1, end)
		ans.left = sub_sol(start, index_io-1)


		return ans

	post_index = [len(post_oo)-1]
	ans = sub_sol(0, len(post_oo)-1)
	return ans



def construct_bst(post_oo):
	# BST can be constructed with just pre order or post order traversal
	# Time Complexity O(N)

	if not post_oo:
		return None

	ans = TreeNode(post_oo[-1])
	stack = [ans]

	for i in range(len(post_oo)-2, -1, -1):
		val = post_oo[i]

		if val > stack[-1].val:
			new_node = TreeNode(val)
			stack[-1].right = new_node
			stack.append(new_node)
		else:
			while stack and stack[-1].val > val:
				popped = stack.pop()
			new_node = TreeNode(val)
			popped.left = new_node
			stack.append(new_node)

	return ans






def main():
	root = TreeNode(1)
	two, three, four, five, seven = TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(7)

	root.left, root.right = two, three
	three.left, three.right = four, five
	five.right = seven

	in_oo = in_order(root)
	print "in_oo ", in_oo

	pre_oo = pre_order(root)
	print "pre_oo ", pre_oo

	post_oo = post_order(root)
	print "post_oo ", post_oo

	new_root = construct_in_pre(in_oo, pre_oo)
	print post_order(new_root)

	new_root = construct_in_post(in_oo, post_oo)
	print pre_order(new_root)


	post_oo = [1,7,5,50,40,10]
	new_root = construct_bst(post_oo)
	print in_order(new_root)
	print pre_order(new_root)

if __name__ == '__main__':
    main()
