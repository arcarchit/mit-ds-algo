

def oneD(heights, fountains):
	"""
	Input :
	h = [1,3,5,3,4]
	f = [f f T f f]

	Output:
	[T T T T f]

	Thinking
	1) If terrain has fountain it will be flooded
	2) If a terrain has immediate bigger neigbour which is also flooded, that terain will also get flooded

	Test Case:
	1) 1 1 1 1 T T T T
	2) 1 T
	3) 1 F


	Complexity : O(N)

	:return:
	"""
	ans = [False]*len(heights)

	for index in range(len(heights)):
		if fountains[index] and not ans[index]:
			ans[index] = True
			# Propgate left
			current, left = index, index - 1
			while left >= 0 and heights[left] <= heights[current]:
				ans[left] = True
				current, left = left, left-1
			current, right = index, index + 1
			while right < len(heights) and heights[right] <= heights[current]:
				ans[right] = True
				current, right = right, right + 1

	return ans







def twoD(heights, fountains):
	"""
	Terrain:
	1 7 1
	3 5 7
	1 3 1

	Has Fountain
	F F F
	F T F
	F F F

	Ans
	T F F
	T T F
	T T T

	:return:
	"""
	ans = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]

	def get_neighbours(row, col):
		candidates = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
		ans = []
		for r,c in candidates:
			if r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0]):
				ans.append((r,c))
		return ans

	def propogate(row, col):
		nn = get_neighbours(row, col)
		for r,c in nn:
			if heights[r][c] <= heights[row][col] and not ans[r][c]:
				ans[r][c] = True
				propogate(r,c)


	for row in range(len(heights)):
		for col in range(len(heights[0])):
			if fountains[row][col] and not ans[row][col]:
				ans[row][col] = True
				propogate(row, col)
	return ans


def fountain2D(height, fountain):
	# Return 2D array of same size
	# Complexity : O(N*M)
	# Complexity of BFS : O(N*M + N*M) = O(N*M)
	ans = [[False for _ in range(len(height[0]))] for _ in range(len(height))]

	def get_neighbours(row, col):
		candidates = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
		ans = []
		for r,c in candidates:
			if r >= 0 and r < len(height) and c >= 0 and c < len(height[0]):
				ans.append((r,c))
		return ans


	def perform_BFS(i, j, ans):
		frontier = [(i,j)]

		visited = set()
		while frontier:
			new_frontier = []
			neighbours = get_neighbours(i, j)
			eligible_neighbours = []
			for x,y in neighbours:
				if height[x][y]<= height[i][j] and not ans[x][y]:
					eligible_neighbours.append((x,y))
			for x,y in eligible_neighbours:
				if (x,y) not in visited:
					ans[x][y] = True
					new_frontier.append((x,y))
			frontier = new_frontier

	for i in range(len(height)):
		for j in range(len(height[0])):
			if fountain[i][j] and not ans[i][j]:
				perform_BFS(i, j, ans) # While performing BFS make them True

	return ans



def main():
	h = [1, 3, 5, 3, 4]
	f = [False, False, True, False, False]
	hh = [[1, 7, 1], [3, 5, 7], [1, 3, 1]]
	ff = [[False, False, False], [False, True, False], [False, False, False]]

	print oneD(h, f)
	print twoD(hh, ff)
	print fountain2D(hh, ff)

if __name__=="__main__":
	main()