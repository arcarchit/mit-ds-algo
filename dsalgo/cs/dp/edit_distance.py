def edit_distance(strA, strB):
    # insert A, insert B, delete A, delete B, update A, update B, same
    # In case of longest common sub-sequence problem would be different. It always helps to right recurrence relation
    # It is not important to get answers, more important is understand complexity , starting from bruetforce.
    def sub_sol(i, j):
        if i==len(strA):
            return len(strB) - j
        if j == len(strB):
            return len(strA) - i
        if strA[i]==strB[j]:
            return sub_sol(i+1, j+1)
        else:
            return 1 + min([
                sub_sol(i, j+1), sub_sol(i+1, j)
                ])
    return sub_sol(0,0)


def edit_distance_bu(strA, strB):
    # Key is to have two for loops for intialization
    # You also don't need to check for index out of range
    # Have an idea of what each cell in array stores
    # 1) it can be substring starting from 0 -- that is what we have -- we start from top left
    # 2) String starting given index to the end -- we start from bottom right
    dp = [[None for _ in range(len(strA))] for _ in range(len(strB))]
    for j in range(len(strB)):
        dp[j][0] = j
    for i in range(len(strA)):
        dp[0][i] = i
    for i in range(1, len(strA)):
        for j in range(1, len(strB)):
            best_sub_sol = min(dp[j-1][i-1], dp[j][i-1], dp[j-1][i])
            if strA[i]==strB[j]:
                dp[j][i] = best_sub_sol
            else:
                dp[j][i] = 1 + best_sub_sol
    return dp[-1][-1]


def edit_distance_driver():
    a = "caut"
    b = "wut"
    print edit_distance_bu(a, b)
    print edit_distance("sunday", "saturday")
    print "\n"

if __name__ == "__main__":
	edit_distance_driver()