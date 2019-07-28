# Nearest smaller element
# Have a rule of thumb : always add index into stack and not the actual values


def nearest_smaller2(arr):
	# Here I am adding index in stack and not the values
	# For this problem it may seem less redable but having one rule of thumb is good
	# For area of rectangle having index helps a lot

	# We need to return array as answer
	# Input 2 1 2 3 2 1
	# Output -1 -1 1 2 1 -1
	st, ans = [], []

	for index in range(len(arr)):
		if st:
			if arr[st[-1]] < arr[index]:
				ans.append(arr[st[-1]])
				st.append(index)
			else:
				while st and arr[st[-1]] >= arr[index]:
					st.pop()
				if st:
					ans.append(arr[st[-1]])
				else:
					ans.append(-1)
				st.append(index)
		else:
			ans.append(-1)
			st.append(index)
	return ans


def neareset_smaller(arr):
	# Complexity : O(N)
	st, ans = [], []
	for x in arr:
		if not st:
			st.append(x)
			ans.append(-1)
		else:
			while st:
				peek = st[-1]
				if peek >= x:
					st.pop()
				else:
					ans.append(peek)
					break
			if not st:
				ans.append(-1)
			st.append(x)
	return ans

def area_histogram(ll):
	"""
	Walkthrough/Test Case
	Edge Case
	Complexity
	"""
	st = []
	ans = 0

	for index, val in enumerate(ll):
		if st:
			top = ll[st[-1]]
			if top >= val:
				# We can not continue with top
				while st and ll[st[-1]] >= val:
					popped = st.pop()
					cand = ll[popped] * (index-st[-1]-1) if st else ll[popped]*index # st[-1] -1 is important, (index - popped) is also wrong
					# We want to find index of next smaller bar
					# First we get height, then we get index of next smaller bar on left, we are already on the next smaller bar of right
					ans = max(ans, cand)
		st.append(index)

	index += 1
	while st and st[-1] >= val:
		popped = st.pop()
		cand = ll[popped] * (index - st[-1]-1) if st else ll[popped] * index
		ans = max(ans, cand)

	return  ans

def main():
	ll = [1, 6, 4, 10, 2, 5]
	ans = neareset_smaller(ll)
	print ans
	print nearest_smaller2(ll)

	ll = [6,2,5,4,5,1,6]
	ll2 = [2,1,2,3,1]
	print area_histogram(ll)
	print area_histogram(ll2)



if __name__=="__main__":
	main()