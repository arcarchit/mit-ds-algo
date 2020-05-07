
# https://www.interviewbit.com/mock-interview/36d122ce/problem/?origin=past&problem_id=11
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/


def buy_sell_once(arr):
    """
    Time Complexity : O(N)
    Space Complexity : O(1)
    """
    MIN_INT = -1e10
    MAX_INT = 1e10
    profit = MIN_INT
    min_so_far = MAX_INT
    for a in arr:
        temp = a - min_so_far
        profit = max(profit, temp)
        min_so_far = min(a, min_so_far)
    return profit

def buy_sell_twice2(arr):
    """
    Time Complexity : O(N)
    Space complexity : O(1)
    :param arr:
    :return:
    """
    # TODO
    pass


def buy_sell_twice(arr):
    """
    s1_profit = profit if we buy and sell by index i.
    s2_profit = profit if we buy and sell sell on/after index i.
    Time Complexity : O(N)
    Space complexity : O(1)
    """
    s1_profit = []
    min_so_far = arr[0]
    max_profit_so_far = 0
    for a in arr:
        temp_profit = a - min_so_far
        max_profit_so_far = max(max_profit_so_far, temp_profit)
        s1_profit.append(max_profit_so_far)
        min_so_far = min(min_so_far, a)


    max_so_far = arr[-1]
    max_profit_so_far = 0


    MIN_INT = -1e10
    ans = MIN_INT
    for i in range(len(arr)-1, -1, -1):
        a = arr[i]
        temp_profit = max_so_far - a
        max_profit_so_far = max(max_profit_so_far, temp_profit)
        max_so_far = max(max_so_far, a)

        temp_ans = s1_profit[i-1] + max_profit_so_far if i>0 else max_profit_so_far
        ans = max(ans, temp_ans)
    return ans


def buy_and_sell_k(arr, k):
    """
    At max k transactions.
    Time Complexity : O(k * N^3)
    Space complexity : O(k * N)

    """


    def sub_sol(i, k):
        """
        Ans for arr[i:]
        :param i:
        :param k:
        :return:
        """
        if k == 0:
            return 0
        if i >= len(arr)-1:
            return 0

        SMALL_NO = -1e6
        ans_total_profit = SMALL_NO
        for b in range(i, len(arr)-1):
            for s in range(b+1, len(arr)):
                current_profit = arr[s] - arr[b]
                future_profit = sub_sol(s+1, k-1)
                total_profit = current_profit + future_profit
                ans_total_profit = max(ans_total_profit, total_profit)
        return ans_total_profit

    ans = sub_sol(0, k)
    return ans

def main():
    arr=[1,4,3,9,6]
    print buy_sell_once(arr)
    print buy_sell_twice(arr)
    arr2 = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    print buy_sell_twice(arr2)
    print buy_and_sell_k(arr2, 3)
    print buy_and_sell_k(arr2, 13)

if __name__=="__main__":
    main()

