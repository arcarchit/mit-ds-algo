



def longest_path(arr):
    # https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
    # Longest path in a matrix

    def get_neighbours(x, y, n):
        ans = []
        if x - 1 >= 0:
            ans.append((x - 1, y))
        if x + 1 < n:
            ans.append((x + 1, y))
        if y - 1 >= 0:
            ans.append((x, y - 1))
        if y + 1 < n:
            ans.append((x, y + 1))
        return ans

    n = len(arr)
    memo = {}

    def sub_sol(x, y):
        n = len(arr)
        # Base Case
        if x<0 or y<0 or x>=n or y >=n:
            return 0

        key = (x, y)
        if key in memo:
            return memo[key]

        neighbours = get_neighbours(x, y, len(arr))
        ans = 1

        for m, n in neighbours:
            if arr[m][n] + 1 == arr[x][y]:
                sol = 1 + sub_sol(m, n)
                ans = max(ans, sol)

        memo[key] = ans
        return ans

    ans = 0
    for i in range(n):
        for j in range(n):
            sol = sub_sol(i, j)
            ans = max(ans, sol)
    return ans



def longest_palindrome(s):
    if not s:
        return 0
    ls = len(s)
    dp = [[-1 for _ in range(ls)] for _ in range(ls)]

    max_len = 1
    for sub_len in range(ls):
        for i in range(ls-sub_len):
            j = i + sub_len
            if i == j:
                dp[i][j] = True
            elif i + 1 == j:
                if s[i] == s[j]:
                    dp[i][j] = True
                    max_len = 2
                else:
                    dp[i][j] = False
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_len = max(max_len, j-i+1)
                else:
                    dp[i][j] = False
    return max_len


def longest_common_substring3(a,b,c):
    la, lb, lc = len(a), len(b), len(c)
    dp = [[[None for _ in range(lc+1)] for _ in range(lb+1)] for _ in range(la+1)]

    MIN_NO = -1e10

    for i in range(la, -1, -1):
        for j in range(lb, -1, -1):
            for k in range(lc, -1, -1):
                if i==la or j==lb or k==lc:
                    dp[i][j][k] = 0
                else:
                    sub_sols = [
                        dp[i+1][j][k],
                        dp[i][j+1][k],
                        dp[i][j][k+1],
                        # dp[i][j+1][k+1], # JUST THESE THREE ARE FINE, ELSE IT WOULD INCREASE TIMECOMPLEXITY UNNECESSARY
                        # dp[i+1][j][k+1],
                        # dp[i+1][j+1][k]
                    ]
                    if a[i]==b[j]==c[k]:
                        sub_sols.append(1 + dp[i+1][j+1][k+1])
                    ans = max(sub_sols)
                    dp[i][j][k] = ans
    return dp[0][0][0]




def longest_path_driver():
    mat = [[1, 2, 9],
           [5, 3, 8],
           [4, 6, 7]]
    print("Length of the longest path is ", longest_path(mat))
    print "\n"

def longest_palindrome_driver():
    print longest_palindrome("ABCDCBE")
    print longest_palindrome("forgeeksskeegfor")
    print "\n"
    

def main():
    longest_path_driver()


if __name__=="__main__":
    main()