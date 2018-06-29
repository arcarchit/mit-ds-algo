

def fibo(n):
    if n <= 2:
        f = 1
    else:
        f = fibo(n-1) + fibo(n-2)
    return f


memo = {}
def fibo_memo(n):
    if n in memo:
        return memo[n]
    if n <=2 :
        f = 1
    else:
        f = fibo(n-1) + fibo(n-2)
    return f


def fibo_up(n):
    ans = {}
    for i in range(1, n+1):
        if i<=2:
            f = 1
        else:
            f = ans[i-1]+ans[i-2]
        ans[i] = f
    return ans[n]


def fibo_save_memory(n):
    pass


print fibo_up(6)