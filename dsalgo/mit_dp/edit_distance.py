"""

Complexity is O(m*n)

# Subproblem = O(m*n)
# Time/subproblem = O(1)

"""


def get_distance_up(s1, s2):

    dp = [[None for i in range(len(s2))] for j in range(len(s1))]



    for i in range(len(s1)-1, -1, -1):
        for j in range(len(s2)-1, -1, -1):
            # print i,j
            if i == len(s1)-1:
                dp[i][j] = len(s2) - j -1
            elif j == len(s2)-1:
                dp[i][j] = len(s1) - i - 1
            else:
                replace = 0 if s1[i] == s2[j] else 1
                replace += dp[i + 1][j + 1]
                add = 1 + dp[i][j + 1]
                # print i,j
                remove = 1 + dp[i + 1][j]
                ans = min(replace, add, remove)
                dp[i][j] = ans

    return dp[0][0]

def get_distance(s1, s2):

    memo = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    def sub_sol(i, j):
        if i<len(s1) and j<len(s2) and memo[i][j] is not None:
            ans = memo[i][j]
        # Base cases
        elif i==len(s1):
            ans = len(s2) - j
        elif j == len(s2):
            ans = len(s1) - i
        else:
            replace = 0 if s1[i]==s2[j] else 1
            replace += sub_sol(i+1, j+1)
            add = 1 + sub_sol(i, j+1)
            remove = 1 + sub_sol(i+1, j)
            ans = min (replace, add, remove)

        memo[i][j] = ans
        return ans

    ans = sub_sol(0, 0)
    return ans



def main():
    print "Distance between cat and cut is ", get_distance_up("cat", "cut")
    print "Distance between geek and gesek is ", get_distance_up("geek", "gesek")
    print "Distance between sunday and saturday is ", get_distance_up("sunday", "saturday")

    print "Distance between cat and cut is ", get_distance("cat", "cut")
    print "Distance between geek and gesek is ", get_distance("geek", "gesek")
    print "Distance between sunday and saturday is ", get_distance("sunday", "saturday")

if __name__ == "__main__":
    main()