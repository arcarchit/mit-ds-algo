# Nearest smaller element

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


def area_histogram(arr):
	# Time Complexity : O(N)

	def get_smaller(ll):
		# returns index of next smaller on left side
		st, ans = [], []
		for i,x in enumerate(ll):
			if not st:
				ans.append(-1)
				st.append(i)
			else:
				while st:
					peek = st[-1]
					if ll[peek] >= x:
						st.pop()
					else:
						ans.append(peek)
						break
				if not st:
					ans.append(-1)
				st.append(i)
		return ans

	left = get_smaller(arr)
	right = get_smaller(list(reversed(arr)))
	right = reversed(right)
	rm = []
	for x in right:
		if x == -1:
			rm.append(-1)
		else:
			rm.append(len(arr) - x - 1)

	ans = -1e10
	for i,x in enumerate(arr):
		if rm[i] == -1 or left[i]==-1:
			continue
		h = x
		w = rm[i] - left[i] - 1
		temp = h*w
		ans = max(ans, temp)
	return ans






def main():
	ll = [1, 6, 4, 10, 2, 5]
	ans = neareset_smaller(ll)
	print ans
	ll = [6,2,5,4,5,1,6]
	ans = area_histogram(ll)
	print ans


if __name__=="__main__":
	main()