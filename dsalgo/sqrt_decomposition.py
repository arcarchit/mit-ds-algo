"""
Suppose you have a sorted array and you want to find sum of numbers between (10,30).
One way is to do binary search twice and sum of all numbers between two indices. Complexity O(N)

Another thing is have sum ready for segments. Optimal way to do this would be
to have segment of size (sqrt N) and there will be total (sqrt N) segments.

Or we can store the sum for index (0:n) and all we need is just subtraction. Time Complexity O(1), space complexity O(N)
But what if we change the element at index i. We need to update all sums. Time Complexity O(N)

SQRT decomposition provides balance between updates and query.
"""

from math import sqrt

class SQRTdeComp:

	def __init__(self, arr):
		self.arr = arr
		self.sum_array = []
		self.bin_len = int(sqrt(len(arr)))
		self.initialize()

	def get_bin(self, index):
		bin = index//self.bin_len
		return bin

	def get_start_end(self, bin):
		# Return given bin start and end indices of the bin
		start = bin * self.bin_len
		end = min((bin+1) * self.bin_len, len(self.arr))
		return (start, end) # end is not inclusive

	def initialize(self):
		for bin_index in range(0, len(self.arr), self.bin_len):
			sum = 0
			for i in range(bin_index, bin_index+self.bin_len):
				sum += self.arr[i]
			self.sum_array.append(sum)

	def update(self, index, new_val):
		old_val = self.arr[index]
		self.arr[index] = new_val
		bin = self.get_bin(index)
		self.sum_array[bin]  += (new_val - old_val)

	def get_sum(self, i, j):
		bin_i, bin_j = self.get_bin(i), self.get_bin(j)

		sum = 0
		for bin in range(bin_i+1, bin_j): sum += self.sum_array[bin]

		si, ei = self.get_start_end(bin_i)
		for index in range(i, ei) : sum += self.arr[index]

		sj, ej = self.get_start_end(bin_j)
		for index in range(sj, j) : sum += self.arr[index]

		return sum


def main():
	arr = [1,2,3,4,5,6,7,8]
	robot = SQRTdeComp(arr)
	print robot.get_sum(0,2)
	print robot.get_sum(1,7)
	robot.update(3,10)
	print robot.get_sum(0, 2)
	print robot.get_sum(1, 7)


if __name__ == '__main__':
    main()