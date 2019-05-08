"""
Disjoint set also means union find algorithm.

Element is index, values is parent. Two items are connected if their ultimate parent is same.
We initialize array with each element is its own parent.

Issue :
Small care needs to be taken care while merging otherwise it will form a chain.
Solution:
1) Union by rank
2) Path compression (Flattens tree in find)

https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

COMPLEXITY ?
Naive approach can have complexity of O(n)
Just using rank bring down time complexity to O(log n)
Using both rank and path compression makes it almost complex
"""



class DisjointSet():

    def __init__(self, n):
        """
        :param n: No of elements in set, starts from 0
        """
        self.ary = [i for i in range(n)]
        self.rank = [0 for i in range(n)]


    def union(self, x, y):
        parent_y = self.find_parent(y)
        parent_x = self.find_parent(x)

        if self.rank[parent_x] < self.rank[parent_y]: # UNION BY RANK
            self.ary[parent_x] = parent_y
            self.rank[parent_y] += 1
        else:
            self.ary[parent_y] = parent_x
            self.rank[parent_x] += 1  # INCREASE RANK


    def find_parent(self, x_in):
        "find parent of x"
        x = x_in
        parent_x = self.ary[x]
        while parent_x != x:
            x = parent_x
            parent_x = self.ary[x]
        self.ary[x_in] = parent_x # PATH COMPRESSION
        return x


    def in_same_set(self, x, y):
        parent_x = self.find_parent(x)
        parent_y =  self.find_parent(y)
        return parent_x==parent_y


    def get_sets(self):
        dicc = {}
        for i in range(len(self.ary)):
            x = self.find_parent(i)
            if x in dicc:
                dicc[x].append(i)
            else:
                dicc[x] = [i]
        return dicc.values()



def main():
    ds = DisjointSet(10)
    ds.union(1,2)
    ds.union(5,6)
    ds.union(8,7)
    print ds.get_sets()
    ds.union(5,7)
    print ds.ary
    print ds.get_sets()
    print ds.in_same_set(1,3)
    print ds.in_same_set(1,2)
    print ds.in_same_set(6,8)

if __name__=="__main__":
    main()

