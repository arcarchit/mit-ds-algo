"""




# Driver code to test above methods
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = construct(freq,len(freq))
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5)))
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6)
print("Sum of elements in arr[0..5]"+
                    " after update is " + str(getsum(BITTree,5)))


"""

class fennwick_tree:

    def __init__(self, ary):
        self.ary = ary
        self.tree = [0]*(len(ary) + 1)
        self.build_tree()

    def build_tree(self):
        for i,val in enumerate(self.ary):
            self.update(i, val)

    def get_sum(self,index):
        # return prefix sum till index (innclusive)
        index += 1
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index = self._parent(index)
        return ans

    def _parent(self, i):
        return i - (i & (-i))

    def _next(self, i):
        return i + (i & (-i))

    def update(self, index, diff):
        # update ary with new values, propgate effect to tree as well
        index += 1
        while index < len(self.tree):
            self.tree[index] += diff
            index = self._next(index)


# below is my solution on leetcode
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update_diff(i + 1, nums[i])

    # parent = i - (i & -i)
    # next = i + (i & -i)

    def update_diff(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff
            i = i + (i & -i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.update_diff(i + 1, diff)

    def get_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i = i - (i & -i)
        return ans

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_sum(j + 1) - self.get_sum(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


def main():
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = fennwick_tree(freq)
    a1 = tree.get_sum(5)
    tree.update(3,6)
    freq[3] += 6
    a2 = tree.get_sum(5)
    print "\n",a1, a2


if __name__=='__main__':
    main()
