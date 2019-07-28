# TODO
# https://leetcode.com/problems/maximum-gap/


def maximum_gap(arr):
	"""
	Idea
	There are N elements
	Have (N-1) partition
	Max distance between partition would be range//(N-1)
	We then just need to find distance between consecutive partitions.

	Things to check, partitoining and indexing
	Walkthrough/Test Case
	[3,6,9,1]
	minn = 1, maxx=9, n = 4, rangg = 8
	buckets = [None, None, None, None]
	[None, [3,3], None, None]
	[None, [3,3], [6,6], None]

	Edge Case
	[], [3], [4,3], [1,3,2]

	Complexity
	"""

	n = len(arr)
	if n==0:
		return 0

	minn, maxx = min(arr), max(arr)
	rangg = maxx - minn

	if n < 2 or rangg==0:
		return 0

	size = rangg//(n-1)
	no_of_buckets = rangg//(size + 1)
	buckets = [None]*no_of_buckets

	for no in arr:
		bucket_index = (no-minn) // size
		bb = buckets[bucket_index]
		if not bb:
			buckets[bucket_index] = [no, no]
		else:
			bb[0] = min(bb[0], no)
			bb[1] = max(bb[1], no)

	ans = size
	buckets = [b for b in buckets if b]
	for i in range(len(buckets)-1):
		j = i+1
		cand = buckets[j][0]-buckets[i][1]
		ans = max(ans, cand)

	return ans




if __name__ == '__main__':
	arr = [1,1000000]
	ans = maximum_gap(arr)
	print ans