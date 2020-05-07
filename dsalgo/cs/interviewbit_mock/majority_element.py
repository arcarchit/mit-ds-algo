def say_hello():
    print 'Hello, World'


for i in xrange(5):
    say_hello()


def majority_element(arr):
    """
    Test Case : [1 1 2 3 1 1] i=0 k=5, i=0 k=4, i=0, k=3 [1 3 2 1 1 1] i=2, k=5 [1 3 2 1 1 1] i=4 k=5 , i=4 k=4
    Edge Case : [1 1 2] i=0,j=2,k=2 [1 2 1] i=2,k=2
    Complexity

    Input : array
    Output : Integer

    array is non empty
    majority element always exists

    Defination : element appears for than floor(n/2)

    n = 4 it appears more than 2
    n = 3 if appears more than 1
    n = 5 if appears more than 2
    n = 6 it appears more than 3

    1) Approach 1
    Iterate through array keep adding in dictionary. Iterate dictionary.
    Time Complexity O(N)
    Space complexity O(N/2) all other elements are distinct

    This can be done to find element with maximum occurance. Does not need to be majority.

    How can the fact that it appears more than floor(n/2) help us ?

    I believe we might not be able to reduce time complexity, but we can reduce sapce complexity.

    2) Approach 2

     1 1 2 3 1 1
        1 3 2 1 1 1

     1 1 2 1 2 1
        1 2 2 1 1 1

     1 1 1 1 2 3
        1 3         1 1 2 1
        1 3         1 2 1 1


    """
    i = 0  # everything before i is discarded
    j = len(arr) - 1
    k = j
    # Ans lies in range i:j inclusive

    while i < k:
        if arr[i] == arr[k]:
            k = k - 1
        else:
            arr[j], arr[i + 1] = arr[i + 1], arr[j]
            k = j
            i = i + 2
    ans = arr[k]
    return ans


def majorityElementCand(A):
    # Sort the array
    # Median element -> Majority Element
    # O(NlogN)

    # Hashmap => count > len(Array) -> majority
    # O(N) O(N)

    L = len(A)
    if L == 0:
        return 0

    stack = list()
    for i in range(L):
        if len(stack) == 0:
            stack.append([A[i], 1])
        else:
            if stack[-1] == A[i]:
                stack[-1][1] += 1
            elif stack[-1] != A[i] and stack[-1][1] > 1:
                stack[-1][1] -= 1
            else:
                stack.pop()
        print stack
    if len(stack) == 0:
        return 0
    return stack[-1][0]



