def matrix_multiplication(dims):
    """Return no of multiplications require"""
    # 10, 30, 20, 40, 20
    x = dims[:-1]  # 10, 30, 20, 40
    y = dims[1:]  # 30, 20, 40, 20

    memo = {}

    def sub_sol(start, end):
        if start + 1 == end:
            return 0
        key = (start, end)
        if key in memo:
            ans = memo[key]
        else:
            min_cost = 1e16
            for k in range(start + 1, end):
                sub_sol1 = sub_sol(start, k)
                sub_sol2 = sub_sol(k, end)
                cost = sub_sol1 + sub_sol2 + x[start] * x[k] * y[end - 1]
                min_cost = min(min_cost, cost)
                ans = min_cost
                memo[key] = ans
        return ans

    return sub_sol(0, len(x))


def matrix_multiplication_bu(dims):
    # 2D dp
    # dp[i][j] = min(cost + dp[i][k] + dp[k][j] for k in range(i, j))
    # What each cell we store
    # dp[i][j] = cost for dims[i:j]
    # Trajectory = It will be triangular dp
    # Trajectory = from bottom right
    # dims = 10, 30, 20, 40, 20

    x = dims[:-1]  # 10 30 20 40
    y = dims[1:]  # 30 20 40 20

    dp = [[0 for _ in range(len(x))] for _ in range(len(x))]

    for row in range(len(x) - 1, -1, -1):
        for col in range(row, len(x)):
            if row == col:
                dp[row][col] = 0

            else:
                ans_cost = 1e10
                for k in range(row, col):
                    cost = dp[row][k] + dp[k + 1][col] + x[row] * y[k] * y[col]
                    ans_cost = min(ans_cost, cost)
                dp[row][col] = ans_cost
    return dp[0][-1]

def matrix_multiplication_driver():
    dims = [40, 20, 30, 10, 30]
    print matrix_multiplication(dims)
    print matrix_multiplication_bu(dims)
    print "\n"


if __name__ == "__main__":
	matrix_multiplication_driver()