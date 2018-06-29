"""
Complexity is O(n^3)

# Subproblems = O(n^2)
# choices = O(n)
# time/subproblem = O(n)


"""

from sys import maxint

def solve_up(ll):
    mm = ll[:-1]
    nn = ll[1:]

    dp = [[None for i in range(len(mm))] for i in range(len(mm))]
    children = {}

    for i in range(len(mm), -1, -1):
        for j in range(i, len(mm)):
            if i == j:
                dp[i][j] = 0
            elif i == (j-1):
                dp[i][j] = mm[i] * mm[j] * nn[j]
            else:
                temp = maxint
                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k+1][j]
                    mid = mm[i] * nn[k] * nn[j]
                    ans = left + right + mid
                    if ans < temp:
                        best_k = k
                        temp = ans
                parent_ss = (i, j)
                child1 = (i, best_k)
                child2 = (best_k + 1, j)
                children[parent_ss] = [child1, child2]
                dp[i][j] = temp

    return dp[0][len(mm)-1], children

def solve(ll):
    mm = ll[:-1]
    nn = ll[1:]

    memo = [[None for i in range(len(mm))] for j in range(len(mm))]
    children = {}

    def sub_sol(i, j):
        if memo[i][j] is not None:
            return memo[i][j]
        if i == (j-1):
            ans = mm[i]*nn[i]*nn[j]
        elif i == j:
            ans = 0
        else:
            ans = maxint
            for k in range(i, j):
                left = sub_sol(i, k)
                right = sub_sol(k+1, j)
                mid = mm[i]*nn[j]*nn[k]
                temp = left + right + mid
                if temp < ans:
                    best_k = k
                    ans = temp
            parent_ss = (i, j)
            child1 = (i, best_k)
            child2 = (best_k + 1, j)
            children[parent_ss] = [child1, child2]
        memo[i][j] = ans
        return ans

    rr =  sub_sol(0, len(mm)-1)
    return rr, children


def pretty_print(dicc, current, level = 0):
    for i in range(level):
        print "  ",
    print current
    if current in dicc:
        for x in dicc[current]:
            pretty_print (dicc, x, level + 1)

def main():
    p = [40, 20, 30, 10, 30]
    print "\n", p
    ans, children = solve_up(p)
    print ans
    parent = (0, len(p) - 2)
    pretty_print(children, parent, 0)

    p = [40, 20, 30, 10, 30]
    print "\n", p
    ans, children = solve(p)
    print ans
    parent = (0, len(p) - 2)
    pretty_print(children, parent, 0)

    q = [10, 20, 30, 40, 30]
    print "\n", q
    ans, children = solve(q)
    print ans
    parent = (0, len(q) - 2)
    pretty_print(children, parent, 0)

if __name__=="__main__":
    main()