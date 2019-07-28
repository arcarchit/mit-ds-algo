# https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
# My solution was dp only, just not a clean code.
# Realizing it is dp, it would be easier to write clean code

# https://leetcode.com/discuss/interview-experience/311906/facebook-intern-1st-interview


def maximum_sum_linear(arr):
	"""
	Our solution is the best.
	This problem is also used to illustrate divide and conquer classically having complexity O(N log N).
	"""

	if not arr:
		return -1

	prev = -10**8
	curr = 0
	ans = prev
	for no in arr:
		if no < 0:
			so_far = max(prev, curr)
			ans = max(ans, so_far, no)
			prev = so_far + no
			curr = 0

		else:
			prev += no
			curr += no
	ans = max(ans, so_far, no)
	return ans



def max_sum_circular(arr):
	"""
	https://www.techiedelight.com/maximum-sum-circular-subarray/
	https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/

	Idea is to apply linear algorithm two times.
	First to find out maximum sum without ends.
	Then we want to find out min sum and subtract it from total sum. This will given possible sum with ends.
	# TODO
	"""
	ll = arr+arr
	print ll
	ans = maximum_sum_linear(ll)
	print ans


if __name__ == '__main__':
	ll = [-2, -5, 6, -2, -3, 1, 5, -6]
	print maximum_sum_linear(ll)
	a = [8, -8, 9, -9, 10, -11, 12]
	max_sum_circular(a)