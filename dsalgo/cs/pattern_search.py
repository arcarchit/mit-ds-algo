

def naivee(text, pattern):
	# Return array of positions
	ans = []
	lt, lp = len(text), len(pattern)
	for i in range(lt - lp + 1):
		j, k = 0, i
		while j < lp:
			if text[k] != pattern[j]:
				break
			j, k = j+1, k + 1
		if j == lp:
			ans.append(i)
	return ans


def kmp(text, pattern):
	# Time complexity O(n + m) = O(n) we exclude O(m) of preprocessing
	# Outer loop increases j by +1, total i time
	# logic can decremtn j by -m
	# WOrst case is when i and j go fully through the step O(2 *n) = O(n)
	# LPS = longest common prefix which is also suffix


	def pre_process():
		# Time Complexity O(m) where m = len(pattern)
		lps = [0] * len(pattern)
		j, i = 0, 1
		while i < len(pattern):
			if pattern[j] == pattern[i]:
				lps[i] = j + 1
				j, i = j + 1, i + 1
			else:
				if j == 0:
					lps[i] = 0
					i = i + 1
				else:
					j = lps[j - 1]

		return lps


	ans = []
	lps = pre_process()
	# print pattern, lps
	lt, lp = len(text), len(pattern)
	i, j = 0, 0
	while i < lt :
		if text[i] == pattern[j]:
			i, j = i + 1, j + 1

		if j == len(pattern):
			ans.append(i - j)
			j = lps[j - 1]
		elif i < lt and text[i] != pattern[j]:
			if j == 0:
				i = i + 1
			else:
				j = lps[j - 1]
	return ans


def rabin_karp(text, pattern):
	# Time complexity O(m*n) all hash passes
	# Excels in plagiarism
	# Multiple patterns to match to

	# Reason for prime
	# https://cs.stackexchange.com/questions/28019/why-is-the-base-used-to-compute-hashes-in-rabin-karp-always-primes
	# If no is prime, chances of other nos being relatively prime to it increases
	# Which helps in uniform frequency distribution
	# Hash = c1 * pow(d^k) + c2 * pow(d^(k-1)) + c3 * pow(d^(k-2)) + . . . . + c_(k-1) * pow(d^1) + c_k * pow(d^0)

	len_text, len_pattern = len(text), len(pattern)

	d, prime = 256, 101

	# Calculate hash of pattern and first window
	pattern_hash, window_hash = 0, 0
	for i in range(len(pattern)):
		pattern_hash = d * pattern_hash + ord(pattern[i])
		window_hash = d * window_hash + ord(text[i])
		pattern_hash, window_hash = pattern_hash % prime, window_hash % prime

	ans = []

	def compare(k):
		i = 0
		while i < len(pattern):
			if pattern[i] != text[k]:
				return False
			i, k = i + 1, k + 1
		return True

	if pattern_hash == window_hash:
		if compare(0):
			ans.append(0)

	i = 1
	j = i + len(pattern) - 1

	while j < len(text):
		window_hash = d*window_hash + ord(text[j]) - ord(text[i-1]) * pow(d, len_pattern)
		window_hash %= prime
		if window_hash == pattern_hash:
			if compare(i):
				ans.append(i)
		i, j = i + 1, j + 1

	return ans


def main():
	print "\nnaivee solution"
	print naivee("AABCCAADDEE", "FAA")
	print naivee("AAAAAAAAAAAAAAAAAA", "AAAAA")
	print naivee("AAAAAAAAAAAAAAAAAB", "AAAAB")
	print "\nkmp"
	print kmp("AABCCAADDEE", "FAA")
	print kmp("AAAAAAAAAAAAAAAAAA", "AAAAA")
	print kmp("AAAAAAAAAAAAAAAAAB", "AAAAB")
	print "\nRobin karp"
	print rabin_karp("AABCCAADDEE", "FAA")
	print rabin_karp("AAAAAAAAAAAAAAAAAA", "AAAAA")
	print rabin_karp("AAAAAAAAAAAAAAAAAB", "AAAAB")


if __name__=="__main__":
	main()