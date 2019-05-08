# https://leetcode.com/problems/the-skyline-problem/


import bisect
import heapq

class PQ:
	# Min Queue
	def __init__(self):
		self.heap = []


	def push(self, item):
		self.heap.append(item)
		self.decrease_key(len(self.heap)-1)


	def decrease_key(self, index):
		pass


	def empty(self):
		# Return True if empty else False
		pass

	def pop(self):
		# Return min element
		pass




def sky_line(self, buildings):
	# Add all buildings to PQ (1, start, height), (3, end, height)
	# Get the point with smallest x values
	# If it changes height it can be critical point, for start it should increase current height, while end will decrease current height
	pq = []
	for b in buildings:
		heapq.heappush(pq, (b[0], 0, b[2]))
		heapq.heappush(pq, (b[1], 1, b[2]))

	current_height = 0
	ans = []

	while pq:
		item = heapq.heappop(pq)
		if item[1] == 0:
			#start
			if item[2] > current_height:
				ans.append((item[0], item[2]))
				current_height = item[2]
		else:
			#end
			if item[2] < current_height:
				ans.append((item[0], item[2]))
				current_height = item[2]

	return ans



def getSkyline(self, buildings):
	"""
	:type buildings: List[List[int]]
	:rtype: List[List[int]]


	1)

	Sort bulinds by starting point
	Take the first one
	Take the second
	DOes first one ends before second one start
	Does height of second < or > height of first one

	We need maintain record of all building which have not yet ended


	2)

	Keep adding new builiding one by one
	O(N^2)

	3)
	Cretae a range tree for how many building can come in given range

	4) Cut the plan at x=mid, create new bilding in both half if there is overlap
	Solve and combine

	Edge Cases :
	# TODO


	Complexity :
	# TODO

	"""

	def sub_sol(start, end, buildings):
		# print start, end, len(buildings)
		# Base case
		if len(buildings) == 1:
			ans = [[start, buildings[0][1]], [end, 0]]
			return ans
		elif start + 1 == end:
			mm = -1
			for x in buildings: mm = max(mm, x[2])
			ans = [[start, mm], [end, 0]]
			return ans


		mid = (start + end ) /2

		# Below can be done in O(log N) using binary search
		# For now stop thinking about space complexity

		# Left buildings end <=mid
		end_sorted = sorted(buildings, key=lambda x :x[1])
		ll = [x[1] for x in end_sorted]
		left_index = bisect.bisect_right(ll, mid)
		left_buildings = end_sorted[:left_index]

		# Right buildings start >= mid
		start_sorted = sorted(buildings, key=lambda x :x[0])
		rr = [x[0] for x in start_sorted]
		right_index = bisect.bisect_left(rr, mid)
		right_buidings = start_sorted[right_index:]

		# Overlapping buildings
		focus_buildings = start_sorted[:right_index]
		focus_end_sort = sorted(focus_buildings, key=lambda x :x[1])
		fee = [x[1] for x in focus_end_sort]
		index = bisect.bisect_right(fee, mid)
		overlapping = focus_end_sort[index:]

		for x in overlapping:
			x_left, x_right = list(x), list(x)
			x_left[1], x_right[0] = mid, mid
			left_buildings.append(x)
			right_buidings.append(x)




		s1 = sub_sol(start, mid, left_buildings)
		s2 = sub_sol(mid, end, right_buidings)

		if s1[-1][1] == s2[0][1] : # Comparing heights, last of left, first of right:
			s1.extend(s2[1:])
		else:
			s1.extend(s2)

		return s1


	start = buildings[0][0]
	end = buildings[-1][1]

	ans = sub_sol(start, end, buildings)

	return ans



def main():
	buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
         (19,18,22), (23,13,29), (24,4,28)]
	points = sky_line(buildings)
	print points


if __name__=="__main__":
	main()

#
#
# Input: Array of buildings
#        { (1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
#          (19,18,22), (23,13,29), (24,4,28) }
# Output: Skyline (an array of rectangular strips)
#         A strip has x coordinate of left side and height
#         (1, 11), (3, 13), (9, 0), (12, 7), (16, 3), (19, 18),
#         (22, 3), (25, 0)