# You were creating tree which is always exponential
# Thier recursion is still okay
# It is like, instead of level order you are doing depth first, later requires lesser memory and iteration


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

def main():
	starting = 3
	no_of_hops = 100
	print count_sequences(starting, no_of_hops)
	print count_sequences_rec(starting, no_of_hops)
	print knight_dialer(no_of_hops, starting)


if __name__=="__main__":
	main()