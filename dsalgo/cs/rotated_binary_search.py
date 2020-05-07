def sol(arr, ele):
    """
    Test Case

    Edge Case
    [1] 1
    [1] 4
    [1,2,3]

    Complexity : O(log N)
    """

    def binary_search(left, right):
        while left < right:
            mid = (left + right+1)/2 # bias to left
            if arr[mid] > ele:
                right = mid - 1
            elif arr[mid] < ele :
                left = mid
            else:
                return mid
        return None

    # binary search to find valley
    valley_index = None
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right+1) / 2  # bias to right
        if arr[mid] > arr[left]:
            left = mid
        else:
            right = mid - 1

    if left != len(arr) - 1:
        valley_index = left

    if valley_index:
        ans1 = binary_search(0, valley_index)
        ans2 = binary_search(valley_index + 1, len(arr) - 1)
        """
        No need to search in both arrays
         (a) If element is greater than 0th element then
             search in left array
          (b) Else Search in right array
              (1 will go in else as 1 < 0th element(3))
        """
        ans = ans1 or ans2
    else:
        ans = binary_search(0, len(arr) - 1)
    return ans if ans else -1


def main():
    arr = [16,22,25,1,2,5,7,9,11,13,14]
    ele = 7
    print sol(arr, ele)


if __name__=="__main__":
    main()