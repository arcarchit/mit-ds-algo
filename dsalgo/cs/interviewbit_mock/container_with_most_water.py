# https://www.interviewbit.com/mock-interview/69049afa/problem/?origin=past&problem_id=169

def solution(arr):
    """
    input : array
    return : int

    [1,5,4,3]
    I had unnecessary went for dp, it was two pointer solution.

    Brute-force approach is to take up all pairs and calculate area.
    Time Complexity : O(N^2)

    When you are reducing width, no point of compromising with height.
    """
    ans = -1
    left, right = 0, len(arr)-1
    while left<right:
        width = right - left
        height = min(arr[left], arr[right])
        area = width * height
        ans = max(ans, area)
        if height == arr[left]:
            left += 1
        else:
            right -= 1
    return ans