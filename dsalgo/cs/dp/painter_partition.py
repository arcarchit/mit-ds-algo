# TODO : Recover parition position

def painter_partition(arr, k):
	# Time Complexity : O(k * N^2)
	# Space Complexity : O(N) for storing the sum array

	BIG_NO = 10**8
	memo = {}

	sum_helper = [0]*len(arr)
	sum_helper[0] = arr[0]

	for index in range(1, len(arr)):
		sum_helper[index] = sum_helper[index-1] + arr[index]


	def sub_sol(last_index, k):
		key = (last_index, k)
		if key in memo:
			ans = memo[key]
		else:
			if k == 1:
				ans = sum_helper[last_index - 1]  # sum(arr[:last_index])
			elif last_index == 1:
				ans = arr[0]
			else:
				ans = BIG_NO
				for index in range(1, last_index):
					c1 = sum_helper[last_index - 1] - sum_helper[index-1] # sum(arr[index:last_index])
					c2 = sub_sol(index, k-1)
					temp = max(c1, c2)
					ans = min(ans, temp)
			memo[key] = ans

		return ans

	ans = sub_sol(len(arr), k)

	return ans



def painter_partition_bu(arr, k):
	dp = [[None for _ in range(len(arr))] for _ in range(k+1)]

	sum_helper = [0] * len(arr)
	sum_helper[0] = arr[0]

	for index in range(1, len(arr)):
		sum_helper[index] = sum_helper[index - 1] + arr[index]

	# dp[k][i] stores ans for k partition with index i inclusive
	for kk in range(k+1):
		for index in range(len(arr)):
			if index == 0:
				dp[kk][index] = arr[index]
			elif kk == 1:
				dp[kk][index] = sum_helper[index]
			else:
				BIG_NO = 10**8
				ans = BIG_NO
				for i in range(1,index+1):
					c1 = sum(arr[i+1:index+1])
					c2 = dp[kk-1][i]
					temp = max(c1, c2)
					ans = min(ans, temp)
				dp[kk][index] = ans

	return dp[-1][-1]


def main():
	arr = [10, 20, 30, 40]
	k = 2
	print painter_partition(arr, k) # Expected 60
	print painter_partition_bu(arr, k)  # Expected 60
	arr = [10, 20, 60, 50, 30, 40]
	k = 3
	print painter_partition(arr, k) # Expected 90
	print painter_partition_bu(arr, k)  # Expected 90


if __name__=="__main__":
	main()