class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):

        if A < 2:
            return str(A)

        import collections
        q = collections.deque()

        def mod(st, N):
            print st
            res = 0
            for x in st:
                extra = 1 if x is '1' else 0
                res = (10 * res + extra) % N
            print st, res
            return res

        q.append('1')
        visited = set()
        while (q):
            candidate = q.popleft()
            res = mod(candidate, A)
            if res == 0:
                return candidate
            elif res not in visited:
                visited.add(res)
                q.append(candidate + '0')
                q.append(candidate + '1')



if __name__=="__main__":
    cc = Solution()
    cc.multiple(55)