# TODo check for optimization

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		def sub_sol(left, right):
			"""
			# Return Tree Node
			left = 0, right = 0, mid = 0
			left = 0, right = 1, mid = 0
			left = 0, right = 2, mid = 1
			left = 1, right = 2, mid = 1

			Complexity : O(N)

			0,4 2
			0,1 & 3,4 -- 0, 3
			0,-1 & 1,1 & 3,2 & 4,4

			0,2 1
			0,0 & 2,2

			"""
			# The second case won't come if we don't have inclusive, right index
			if left == right:
				new_node = TreeNode(nums[left])
			elif left + 1 == right:
				new_node = TreeNode(nums[right])
				new_node.left = TreeNode(nums[left])
			else:
				mid = (right + left) / 2
				new_node = TreeNode(nums[mid])
				new_node.left = sub_sol(left, mid - 1)
				new_node.right = sub_sol(mid + 1, right)
			return new_node

		ans = sub_sol(0, len(nums) - 1)
		return ans


def sortedArrayToBST2(self, nums):
	"""
	:type nums: List[int]
	:rtype: TreeNode
	"""

	if not nums:
		return None

	def sub_sol(left, right):
		"""
		# Return Tree Node
		left = 0, right = 0, mid = 0
		left = 0, right = 1, mid = 0
		left = 0, right = 2, mid = 1
		left = 1, right = 2, mid = 1

		Complexity : O(N)

		Test case :
		1) Empty array
		2) Array with 1,2,3,7 element

		"""
		if left == right:
			new_node = None # You can always return None to simplify things
		else:
			mid = (right + left) // 2
			new_node = TreeNode(nums[mid])
			new_node.left = sub_sol(left, mid)
			new_node.right = sub_sol(mid + 1, right)
		return new_node

	ans = sub_sol(0, len(nums))
	return ans