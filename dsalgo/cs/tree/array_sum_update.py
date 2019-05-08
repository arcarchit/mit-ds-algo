# Both of this tree are represented as array like heap unlike BST.

import math

MAX = 1e10

class SegmentTree:
	# Range query
	# Max, min, sum in certain range

	def __init__(self, ll):
		self.ary = ll
		height = math.ceil(math.log(len(ll), 2))
		len_corrected = int(math.pow(2, height))
		size = 2 * len_corrected - 1
		self.tree_ary = [MAX] * size


	def update_ary(self, index, val):
		if index >= len(self.ary):
			raise Exception("index out of range")

		tree_len = len(self.tree_ary)
		offset = int(math.log(tree_len + 1, 2))
		pos = offset + index

		self.tree_ary[pos] = val
		self.ary[index] = val

		while True:
			pos = (pos-1)/2
			if pos < 0:
				break
			else:
				left_child, right_child = 2*pos + 1, 2*pos + 2
				self.tree_ary[pos] = min(self.tree_ary[left_child], self.tree_ary[right_child])



	def construct_tree(self):
		# Both time complexity and space complexity is O(n)

		def sub_sol(left, right, pos):
			if left == right:
				self.tree_ary[pos] = self.ary[left]
				return

			mid = (left + right)/2
			left_child, right_child = 2*pos+1, 2*pos+2
			sub_sol(left, mid, left_child)
			sub_sol(mid+1, right, right_child)

			self.tree_ary[pos] = min(self.tree_ary[left_child], self.tree_ary[right_child])

		sub_sol(0, len(self.ary) - 1, 0)


	def range_query(self, q_left, q_right):
		def sub_sol(t_left, t_right, pos):
			if t_left >= q_left and t_right<= q_right:
				cand1 = self.tree_ary[pos]
				return cand1
			if t_right < q_left or t_left > q_right:
				return MAX
			t_mid = (t_left + t_right)/2
			left_child, right_child = 2*pos+1, 2*pos+2

			cand1, cand2 = sub_sol(t_left, t_mid, left_child), sub_sol(t_mid+1, t_right, right_child)
			return min(cand1, cand2)

		return sub_sol(0, len(self.ary)-1, 0)


	def print_segment_tree(self):
		print self.tree_ary



class FenwickTree:
	# Also known as binary index tree, takes less space than segment tree
	# But supports just sum, not min or max. (I think so)
	pass



class SQRTdeComp:

	# If array size is fixed (no isert , update allowed) we can use this instead of
	# 1) Segment Tree : O(N log N) time, O(N) space
	# 2) Storing 2D matrix : O(N^2)

	def __init__(self, ll):
		self.ary = ll
		self.n = len(ll)
		self.block_size = int(math.ceil(math.sqrt(self.n)))
		self.blocks = [0] * self.block_size
		self.build()

	def build(self):
		# Complexity O(N)
		for i in range(self.n):
			block_no = i / self.block_size
			self.blocks[block_no] += self.ary[i]
		print self.blocks

	def update(self, index, new_val):
		# Complexity O(1)
		block_no = index / self.block_size
		self.blocks[block_no] += new_val - self.ary[index]
		self.ary[index] = new_val

	def query(self, left, right):
		# Complexity : O(sqrt(N))
		left_block_no, right_block_no = left / self.block_size, right / self.block_size


		left_block_end = min(self.block_size * (left_block_no + 1) - 1, len(self.ary), right)
		right_block_start = self.block_size * right_block_no

		# print left, left_block_end, left_block_no, right_block_no, right_block_start, right
		ans = 0

		for i in range(left, left_block_end +1):
			ans += self.ary[i]

		for i in range(left_block_no+1, right_block_no):
			ans += self.blocks[i]

		if left_block_no != right_block_no:
			for i in range(right_block_start, right + 1):
				ans += self.ary[i]
		return ans

def main():
	ll = [-1, 2, 4, 0]

	st = SegmentTree(ll)
	st.construct_tree()
	st.print_segment_tree()

	print st.range_query(0,3)
	print st.range_query(1,3)

	print "\nupdate\n"
	st.update_ary(2, -2)
	print st.ary
	st.print_segment_tree()

	print st.range_query(0, 3)
	print st.range_query(1, 3)


	ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	sd = SQRTdeComp(ll)
	print sd.query(0, 5) # Expect 21
	print sd.query(1, 3) # 9
	print sd.query(8, 8) # 9
	sd.update(5, 10) #
	print sd.query(6, 6) # 7
	print sd.query(5, 6)  # 17



if __name__=="__main__":
	main()
