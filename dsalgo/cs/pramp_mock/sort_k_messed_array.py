# IMP : This can also be done inplace
# Start inserting from first position. Values are already in heap.

import heapq

def sort_k_messed_array(arr, k):
    """
    Test Case
      given exmaple
    Edge Case : len(ary) 1 or 0
    k = 1, 0

    Time Complexity : O(N log K)
    Space complexity : O(K)

    IMP : This can also be done inplace

    """
    if k < 1 :return arr
    hp = []
    i = 0
    for a in arr:
        if len(hp) == k+ 1:
            popped = heapq.heappop(hp)
            arr[i] = popped
            i = i + 1

        heapq.heappush(hp, a)

    while hp:
        popped = heapq.heappop(hp)
        arr[i] = popped
        i = i + 1

    return arr


