# https://leetcode.com/problems/student-attendance-record-ii/
# https://leetcode.com/problems/student-attendance-record-ii/discuss/101643/Share-my-O(n)-C%2B%2B-DP-solution-with-thinking-process-and-explanation

def student_attendance(n):
	"""
	A,L,P

	A[1] = L[1], P[1] = 1

	T(n) = A(n) + L(n) + P(n)

	P(n) = A(n-1) + L(n-1) + P(n-1)

	L(n) = A(n-1) + P(n-1) + A(n-2) + P(n-2)

	A(n) = noaP(n-1) + noaL(n-1)

	noaP(n) = noaP(n-1) + noaL(n-1) # Ending with P and has no A

	noaL(n) = noaP(n-1) + noaP(n-2)

	noaP(1) = noaL(1) = 1
	noaL(2) = 2, PL, LL

	A[2] = 2 PA, LA
	P[2] = 2 AP, LP


	# +++++++++++

	T(n) = A(n) + L(n) + P(n)

	P(n) = A(n-1) + L(n-1) + P(n-1), P(1) = 1
	L(n) = A(n-1) + P(n-1) + A(n-2) + P(n-2), L(1) = 1, L(2) = 3
	A(n) = noaP(n-1) + noaL(n-1), A(1) = 1

	noaP(n) = noaP(n-1) + noaL(n-1), noaP(1) = 1
	noaL(n) = noaP(n-1) + noaP(n-2), noaL(1) = 1, noaL(2) = 2

	# +++++++++++++

	P(1) = 1
	L(1) = 1, L(2) = 3
	A(1) = 1
	noaP(1) = 1
	noaL(1) = 1, noaL(2) = 2

	Update sequence :

	* P(2) = 3, PP, AP, LP

	noaP(2) = 2
	noaL(2) = 2-- initialized
	* A(2) = 2 LA, PA

	* L(2) = 3, LL, AL, PL -- initialized

	---------------

	* P(3) = 8
	noap(3) = 4
	noaL(3) = 3

	* A(3) = 4
	* L(3) = 7 # sum of (2,3,1,1)


	# +++++++++++

	:param n:
	:return:
	"""


	if n==1:
		return 3
	if n==2:
		# LA, PA, LL, PL, AP, LP, LL, PP
		return 8
	else:

		a,p,l = 4,8,7
		noL, noP = 3,4
		prev_A, prev_P, prev_noP = 2,3,2

		i = 3
		while i<n:
			i += 1

			next_P = a + p + l
			next_noP = noP + noL
			next_noL = noP + prev_noP
			next_A = noP + noL
			next_L = a + p + prev_A + prev_P

			prev_A, prev_P, prev_noP = a, p, noP
			a,p,l,noL,noP = next_A,next_P,next_L,next_noL,next_noP

		return a + p + l


def main():
	n = 4
	ans = student_attendance(n)
	print ans

if __name__=="__main__":
	main()

