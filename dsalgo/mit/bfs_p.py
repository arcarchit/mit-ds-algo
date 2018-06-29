from heapq import *


h = []
heappush(h, 3)
heappush(h, 5)
heappush(h,4)

ss = set([2, 3, 4, 5, 7, 2])
print h[0], h[1], h[2]

print nlargest(2, h)
print nsmallest(2, h)
print nsmallest(3, ss)

qq = set()
qq = qq.union(ss)

print heappop(h)
print heappop(h)



