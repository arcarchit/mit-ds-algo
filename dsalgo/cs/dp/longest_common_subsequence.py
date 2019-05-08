# Longest common substring : Bruteforce O(n * m^2)  DP O(mn)
# Longest common subsequence : Bruteforce O(2^n)  DP O(mn)

# Exponential is worse than polynomial


# Complexity of LCS-3 would be O(mnp) ~ O(m^3)
# Complexity of LCS-4 would be O(m^4)
# COmplexity of LCS-n would be O(m^n) which is exponential, this is NP complete problem.


def lcss_dp(strA, strB):
	"""
	dp(i, j)

	if strA[i] == strB[j]:
		dp(i-1, j-1) + 1, suffix should end at i-1, j-1

	sub_sol(i, j) = longest common suffix, ending at (i,j)

	ans = max over all (i,J) => O(mn)


	:param strA:
	:param strB:
	:return:
	"""

	memo = {}
	def sub_sol(i,j):
		key = (i, j)
		if key in memo:
			return memo[key]

		if i<0 or j<0:
			ans = (0, 0, 0)
		elif strA[i] == strB[j]:
			val = 1 + sub_sol(i-1, j-1)[0]
			ans = (val, i, j)
		else:
			ans = (0,0,0)
		memo[key] = ans
		return ans

	ans = -1
	for i in range(len(strA)):
		for j in range(len(strB)):
			candidate = sub_sol(i, j)
			ans = max(ans, candidate)
	return ans



def longest_common_subsequence(strA, strB):
	# Return longest common subsequence
	"""

	abc & pqr => ""
	abcd & pqbr => "b"
	abcpr & bcdwp => "bc"

	Complexity : O(mn)
	"""

	la, lb = len(strA), len(strB)
	memo = {}

	def sub_sol(i, j):
		# We want to return both i and j, not just the length
		# len, i, j
		key = (i, j)
		if key in memo:
			return memo[key]

		if i == la or j == lb:
			return (0, 0, 0)

		if strA[i] == strB[j]:
			len, _, _ = sub_sol(i+1, j+1)
			ans = (1+len, i, j)
			memo[key] = ans
			return ans
		else:
			s2 = sub_sol(i+1, j)
			s3 = sub_sol(i, j+1)
			ans = s2 if s2[0] > s3[0] else s3
			memo[key] = ans
			return ans

	ans = sub_sol(0,0)
	return ans



def lcs3(strA, strB, strC):
	"""
	dp(i,j,k) =

	dp(i+1, j, k)
	dp(i, j+1, k)
	dp(i, j, k+1)
	dp(i+1, j+1, k)
	dp(i+1, j, k+1)
	dp(i, j+1, k+1)
	dp(i+1, j+1, k+1)

	Above 7 are not required, just 3 are needed.

	dp(i+1, j, k)
	dp(i, j+1, k)
	dp(i, j, k+1)

	Rest can be derived from them.

	Complexity : O(mnp)
	"""

	memo = {}
	def sub_sol(i,j,k):
		key = (i,j,k)

		if key in memo:
			return memo[key]

		if i==len(strA) or j == len(strB) or k == len(strC):
			return (0, 0, 0, 0)

		if strA[i] == strB[j] == strC[k]:
			val = 1 + sub_sol(i+1, j+1, k+1)[0]
			ans = (val, i, j, k)
		else:
			s1 = sub_sol(i+1, j, k)
			s2 = sub_sol(i, j+1, k)
			s3 = sub_sol(i, j, k+1)

			ans = max(s1, s2, s3)

		memo[key] = ans
		return ans

	return sub_sol(0,0,0)


def main():
	print "Logest common subsequence"
	print longest_common_subsequence("abc", "pqr")
	print longest_common_subsequence("abcd", "pqbr")
	print longest_common_subsequence("abcpr", "bcdwp")
	print "Longest common substringn"
	print lcss_dp("abc", "pqr")
	print lcss_dp("abcd", "pqbr")
	print lcss_dp("abcpr", "bcdwp")
	print "Longest common subsequence 3"
	print lcs3("abc", "pqr", "xyz")
	print lcs3("abcd", "pqbr", "xbzy")
	print lcs3("abcpr", "bcdwp", "xbyzcp")



if __name__=="__main__":
	main()