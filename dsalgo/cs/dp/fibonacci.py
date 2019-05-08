def fibonacci(n):
    # Time Complexity : O(N)
    # Space Complexity : O(1)
    if n < 1:
        raise ("n must be greater than 1")
    x1, x2 = 1,1
    if n<=2:
        return 1
    i = 2
    while i<n:
        x3 = x1 + x2
        x1, x2 = x2, x3
        i = i + 1
    return x3


def fibonacci_driver():
    for i in range(1, 6):
        print fibonacci(i),
    print "\n"


if __name__=="__main__":
	fibonacci_driver()