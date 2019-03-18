def topdown(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        count = topdown(n - 1) + topdown(n - 2) + topdown(n - 3)
        memo[n] = count
        return count


memo = dict()
for testCase in range(int(input())):
    print(topdown(int(input())))
