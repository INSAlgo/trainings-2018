

def coin_change(n, m):
    if n == 0:
        return 1
    elif n < 0 or (m <=0 and n >= 1):
        return 0
    elif (n, m) in memo:
        return memo[(n, m)]
    else:
        include_last = coin_change(n - coins[m - 1], m)
        exclude_last = coin_change(n, m - 1)
        memo[(n, m)] = include_last + exclude_last
        return include_last + exclude_last


memo = dict()
n, m = map(int, input().split())
coins = list(map(int, input().split()))
print(coin_change(n, m))
