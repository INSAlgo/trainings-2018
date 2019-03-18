cases = []
for testCase in range(int(input())):
    cases.append(int(input()))

dp = [0] * (max(cases) + 1)  # to count from 1 and not 0
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, max(cases) + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for case in cases:
    print(dp[case])
