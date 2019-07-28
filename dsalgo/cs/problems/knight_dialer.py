

def knight_dialer(no_of_hops, starting):
	# Return how many distinct no, you can dial
	# Time complexity
	# 1 + 2 + 4 + 8 + . . . + 2 ^n
	dic = {
		0: [4, 6],
		1: [6, 8],
		2: [7, 9],
		3: [4, 8],
		4: [3, 9, 0],
		5: [],
		6: [1, 7, 0],
		7: [2, 6],
		8: [1, 3],
		9: [4, 2]
	}

	frontier = [starting]
	hopes = 0
	while frontier:
		new_frontier = []
		for n in frontier:
			for p in neighbors(n):
				new_frontier.append(p)
		frontier = new_frontier
		hopes = hopes + 1
		if no_of_hops == hopes:
			return len(frontier)

NEIGHBORS_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}
def neighbors(position):
	return NEIGHBORS_MAP[position]

def count_sequences(start_position, num_hops):
	prior_case = [1] * 10
	current_case = [0] * 10
	current_num_hops = 1

	while current_num_hops <= num_hops:
		current_case = [0] * 10
		current_num_hops += 1

		for position in range(0, 10):
			for neighbor in neighbors(position):
				current_case[position] += prior_case[neighbor]
		prior_case = current_case


	return current_case[start_position]


def count_sequences_rec(start_position, num_hops):
	if num_hops == 0:
		return 1

	num_sequences = 0
	for position in neighbors(start_position):
		num_sequences += count_sequences(position, num_hops - 1)

	return num_sequences


def take20(start_position, num_hops):
	"""
	Walkthrough
	ok
	Complexity
	O(2^num_hops)

	:param start_position:
	:param num_hops:
	:return:
	"""
	dic = {
		0:[4,6],
		1:[6,8],
		2:[7,9],
		3:[4,8],
		4:[0,3,9],
		5:[],
		6:[0,1,7],
		7:[2,6],
		8:[1,3],
		9:[2,4]
	}

	if num_hops != 0:
		ans = 0
		for no in dic[start_position]:
			ans += take20(no, num_hops-1)
	else:
		ans = 1

	return ans


def take21(start_position, num_hops):
	"""
	Complexity : O(10 * num_hopes) = O(N)
	:param start_position:
	:param num_hops:
	:return:
	"""
	dic = {
		0: [4, 6],
		1: [6, 8],
		2: [7, 9],
		3: [4, 8],
		4: [0, 3, 9],
		5: [],
		6: [0, 1, 7],
		7: [2, 6],
		8: [1, 3],
		9: [2, 4]
	}

	memo = {}
	def sub_sol(pos, num_hops):
		if num_hops == 0:
			return 1
		key = (pos ,num_hops)
		if key in memo:
			ans = memo[key]
		else:
			ans = 0
			for no in dic[pos]: ans += sub_sol(no, num_hops-1)
			memo[key]=ans
		return ans


	ans = sub_sol(start_position, num_hops)
	return ans

def take22(start_position, num_hops):
	"""
	DP bottom up
	# Edge Case (5,2) is also solved, ans is 0, you can't go anywhere
	"""
	dic = {
		0: [4, 6],
		1: [6, 8],
		2: [7, 9],
		3: [4, 8],
		4: [0, 3, 9],
		5: [],
		6: [0, 1, 7],
		7: [2, 6],
		8: [1, 3],
		9: [2, 4]
	}
	memo = [[0 for _ in range(10)] for _ in range(num_hops+1)]
	for j in range(num_hops+1):
		for i in range(10):
			if j==0:
				memo[j][i] = 1
			else:
				for no in dic[i]:
					memo[j][i] += memo[j-1][no]
	return memo[-1][start_position]

def take23(start_position, num_hops):
	"""
	We can save space in DP
	For calculating DP[_,N] we only need DP[_,N-1]
	Space complexity was O(N) previously and now as well. We just reduce it terms of bytes.
	"""
	dic = {
		0: [4, 6],
		1: [6, 8],
		2: [7, 9],
		3: [4, 8],
		4: [0, 3, 9],
		5: [],
		6: [0, 1, 7],
		7: [2, 6],
		8: [1, 3],
		9: [2, 4]
	}
	pre_dp = [1]*10
	for _ in range(num_hops):
		new_dp = [0]*10
		for no in range(10):
			for neighbor in dic[no]:
				new_dp[no]+= pre_dp[neighbor]
		pre_dp = new_dp
	return pre_dp[start_position]


def main():
	starting = 3
	no_of_hops = 100
	print count_sequences(starting, no_of_hops)
	print count_sequences_rec(starting, no_of_hops)
	# print knight_dialer(no_of_hops, starting)
	print take23(starting, no_of_hops)
	print take22(starting, no_of_hops)
	print take21(starting, no_of_hops)
	# print take20(starting, no_of_hops)



if __name__=="__main__":
	main()