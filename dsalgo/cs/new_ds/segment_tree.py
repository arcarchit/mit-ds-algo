

class segment_tree:

    def __init__(self, nums):
        self.nums = nums
        tree_len = self._get_tree_len(len(nums))
        self.tree = [0]*tree_len
        self.build_tree(0, 0, len(nums)-1)


    def build_tree(self, ti, nl, nr):
        if nl == nr:
            self.tree[ti] = self.nums[nl]
        else:
            mid = (nl + nr)/2
            left = self.build_tree(2*ti+1, nl, mid)
            right = self.build_tree(2*ti+2, mid+1, nr)
            self.tree[ti] = left + right
        return self.tree[ti]



    def _get_tree_len(self, no):
        pow2 = 1
        while pow2 < no:pow2 = 2*pow2
        pow2 = 2*pow2
        return pow2-1


    def _get_sum(self, ti, tl, tr, nl, nr):
        if nl <= tl and nr >= tr:
            ans = self.tree[ti]
        elif nl > tr or nr < tl:
            ans = 0
        else:
            mid = (tl + tr)/2
            sub1 = self._get_sum(2*ti+1, tl, mid, nl, nr)
            sub2 = self._get_sum(2*ti+2, mid+1, tr, nl, nr)
            ans = sub1 + sub2
        return ans



    def get_sum(self, i, j):
        ans = self._get_sum(0, 0, len(self.nums)-1, i, j)
        return ans


    def _update(self, ti, tl, tr, i, diff):
        self.tree[ti] += diff
        if tl == tr == i : return
        mid = (tl + tr)/2
        if i <= mid :
            self._update(2*ti+1, tl, mid, i, diff)
        else:
            self._update(2*ti+2, mid+1, tr, i, diff)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self._update(0, 0, len(self.nums)-1, i, diff)






def main():
    freq = [2, 3, 5, 7, 9, 11]
    tree = segment_tree(freq)
    print tree.nums
    print tree.tree

    a1 = tree.get_sum(1,3)
    tree.update(1,10)
    a2 = tree.get_sum(1,3)
    print "\n",a1, a2


if __name__=='__main__':
    main()


