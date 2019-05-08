# This is also know as Fenwick tree.

# https://www.youtube.com/watch?v=CWDQJGaN1gY
#
# https://brilliant.org/wiki/fenwick-tree/


"""
Used in prefix sum.
Prefix sum = Sum of first n elements in array

Naivee approach :
Loop through first n elements and sum up
O(n)

What if array keeps changing and no of queries are more.

Assumption is value keeps changing but no of elements are same.

"""

class BITree:


    def __init__(self, ll):
        self.tree = [0 for _ in xrange(len(ll) + 1)]
        self.N = len(ll)
        for i, val in enumerate(ll):
            self.update(i, val)

    def query_at(self, i):
        index = i+1
        ans = 0
        while index >0:
            ans += self.tree[index]
            parent = index - (index & (-index))  # THIS is bit manipulation trick
            index = parent
        return ans

    def update(self, i, by):
        index = i + 1
        while index <= self.N:
            self.tree[index] += by
            next = index + (index & (-index))   # THIS is bit manipulation trick
            index = next



def main():

    ll = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = BITree(ll)
    print tree.query_at(5)
    # ll[3] += 6
    tree.update(3, 6)
    print tree.query_at(5)


if __name__=="__main__":
    main()

