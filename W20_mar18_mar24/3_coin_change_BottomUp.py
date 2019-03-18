n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[0 for j in range(m)] for i in range(n + 1)]

for i in range(m):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(m):

        includeLast = 0
        excludeLast = 0

        if i - coins[j] >= 0:
            includeLast = dp[i - coins[j]][j]
        if j >=1:
            excludeLast = dp[i][j - 1]

        dp[i][j] = includeLast + excludeLast

print(dp[-1][-1])
