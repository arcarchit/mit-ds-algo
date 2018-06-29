class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):

        # tuple (diff, element, length)
        # desire_element = element - diff
        # a1 = a2 - 4
        dp = []

        for i in range(len(A) - 1, -1, -1):
            naivee = (None, A[i], 1)
            if i == len(A) - 1:
                dp.append(naivee)
                continue
            new_appends = [naivee]
            exclude_set = set()
            for tt in reversed(dp):
                if tt[1] in exclude_set:
                    continue
                if tt[0] == None:
                    ele = tt[1]
                    lenn = tt[2]
                    diff = ele - A[i]
                    new_appends.append((diff, A[i], lenn + 1))
                else:
                    diff = tt[0]
                    desired_ele = tt[1] - diff
                    if (A[i] == desired_ele):
                        exclude_set.add(tt[1])
                        new_appends.append((diff, A[i], tt[2] + 1))
            dp.extend(new_appends)

        ans_len = 0
        for diff, elem, lenn in dp:
            ans_len = max(ans_len, lenn)

        return ans_len

if __name__ == "__main__":
    sol = Solution()
    print sol.solve([9, 4, 7, 2, 10])