def knapsack(values, weights, capacity):
	# Complexity : O(2 ^ N) without memoization
	# WIth memoization it turns out O(capacity * N)

	# First let's write to just written values

	items_taken = [0 for _ in range(len(weights))]

	def sub_sol(index, remaining_capacity, val_so_far): # No need to pass val_so_far in recursion, it should mimic dp. Have global variable. One workaorund it to have memo on first two only.
		if index == len(weights):
			return {
				'val': val_so_far,
				'taken': list(items_taken)
			}
		if remaining_capacity >= weights[index]:
			items_taken[index] = 1
			sol1 = sub_sol(index + 1, remaining_capacity - weights[index], val_so_far + values[index])
			val1, taken1 = sol1['val'], sol1['taken']
			items_taken[index] = 0
		else:
			sol1 = -1

		sol2 = sub_sol(index + 1, remaining_capacity, val_so_far)
		val2, taken2 = sol2['val'], sol2['taken']

		if sol1 > sol2:
			return {
				'val': val1,
				'taken': taken1
			}
		else:
			return {
				'val': val2,
				'taken': taken2
			}

	return sub_sol(0, capacity, 0)


def knapsack_bu(values, weights, capacity):
	# Complexity : O(capacity * N)
	dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights))]

	SMALL_NO = -10 ** 8

	for index in range(len(weights)):
		for c in range(capacity + 1):
			if index == 0:
				if weights[index] <= c:
					dp[index][c] = values[index]
			else:
				v, w = values[index], weights[index]
				# include item
				search_c = c - w  # This is important
				ans1 = (v + dp[index - 1][search_c]) if search_c >= 0 else SMALL_NO

				# exclude item
				ans2 = dp[index - 1][c]

				dp[index][c] = max(ans1, ans2)

	val = dp[-1][-1]

	# Now reconstruct the items taken

	ans = [0] * len(weights)

	for index in range(len(weights) - 1, -1, -1):
		if capacity == 0:
			break
		if index > 0:
			if dp[index][capacity] == dp[index - 1][capacity]:
				# Value is same with and without index item
				# Item is not taken
				ans[index] = 0
			else:
				# Item is taken, subtract weight from capacity
				ans[index] = 1
				capacity = capacity - weights[index]
		else:
			if capacity != 0:
				ans[index] = 1

	return {
		'taken': ans,
		'val': val
	}


def knapsack_driver():
	values = [50, 70, 30, 20, 20, 20]
	weights = [1, 2, 1, 3, 1, 2]
	capacity = 5

	print knapsack(values, weights, capacity)
	print knapsack_bu(values, weights, capacity)
	print "\n"


if __name__ == "__main__":
	knapsack_driver()
