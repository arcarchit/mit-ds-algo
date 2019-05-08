# https://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/

import math, random

def school_method(a):
	# Return weather given no is prime or not
	ans = 0
	for i in range(1, a+1):
		if a%i == 0:
			ans +=1
			if ans > 2:
				return False
	return True


def optimized_school(a):
	x = int(math.ceil(math.sqrt(a))) + 1
	ans = 0
	for i in range(2, x):
		if a%i == 0:
			return False
	return True


def fermat(n):
	# Take a random no a < n
	# if GCD(a, d) != 1 implies a is composite We generally don't check GCD. It can helps increasing odds though.
	# else a^(n-1) mod n != 1 implies a is composite
	# else a can be prime
	# Idea is to have a condition which all prime holds and 99% composite does not hold.
	# if n is prime condition will be hold
	# if n is composite it will be rarely hold, we repeat it NO_ITER time to deduce probability

	# Repeat above t times picking up different d
	# Time Complexity : O(NO_ITER * log n) -- pow function's complexity O(log N)

	if n <= 3:
		return True

	if n % 2 == 0:
		return False

	NO_ITER = 100

	# If n is prime, then ans will be 1
	# If n is not prime
	for _ in range(NO_ITER):
		a = random.randint(1, n-1)

		ans = pow(a, n-1) % n
		if ans != 1:
			return False

	return True


def miller():
	pass



def main():
	ary = [41, 56, 57, 92, 93, 94, 101]
	for a in ary:
		print a, school_method(a), optimized_school(a), fermat(a)



if __name__=="__main__":
	main()