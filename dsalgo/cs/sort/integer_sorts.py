#TODO


# Comments on counting sort
# To handle negative numbers we can change range by adding min to make it 0
# to sort numbers say in range 100 to 200, we can have k = max - min = 200 - 100 = 100. This saves space.


# When keys are not integer (say they are floats) counting sort can not be applied
# We use bucket sort for that

def radix_sort():
	pass


def counting_sort_bad(arr, k=256):
	"""
	Time Complexity : O(n)
	Space complexity L O(k)
	Also will not help to sort object
	"""
	cnt = [0]*k # O(k)

	for x in arr: # O(n)
		cnt[x]+=1

	i = 0
	for j in range(len(cnt)): # I believe this will be O(n) only, n can be small or greter than k.
		if i== len(arr):break
		times = cnt[j]
		while times > 0: # BAD : Nested loops
			arr[i] = j
			i += 1
			times -= 1

	return arr

def counting_sort_good(arr, k=256):
	"""
	We want to know position of object in final ans and store it there.
	This will allows us to sort object as well.
	We had to create auxiliary array ans which will bring space complexity to O(n+k)

	Now both time and space complexity is O(n+k)
	"""
	count = [0]*k
	for x in arr:
		count[x] += 1
	for index in range(1, k):
		count[index] = count[index] + count[index - 1]

	ans = [None]*len(arr)

	for x in arr:
		index = count[x] - 1 #index starts from 0
		ans[index] = x
		count[x] -= 1

	return ans


def insertion_sort_util(arr):
	arr.sort()
	return arr



def bucket_sort(arr, n):
	# Space complexity : O(N), not in place

	buckets = [None]*n
	for i in range(n):
		buckets[i] = list()
	minn, maxx = min(arr), max(arr)
	rangg = maxx - minn + 1
	size = rangg//n

	# devide
	for no in arr:
		bucket_index = min((no-minn)//size, n-1) # THis is important , because last bucket can have reminder of sizes
		buckets[bucket_index].append(no)

	# sort
	for i in range(len(buckets)):
		buckets[i] = insertion_sort_util(buckets[i])

	# combine
	ans = []
	for x in buckets:
		ans.extend(x)

	return ans



if __name__=="__main__":
	arr = [1,3,5, 8,2,7,8,4,9,0,6]
	print len(arr)
	print counting_sort_good(arr)
	print counting_sort_bad(arr)

	arr = [1, 3, 5, 8, 2, 7, 8, 4, 9, 0, 6]
	print  bucket_sort(arr, 3)
	print bucket_sort(arr, 2)
	print bucket_sort(arr, 4)