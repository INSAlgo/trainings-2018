import sys
sys.setrecursionlimit(5000)


def knapsack(c, objects):
    if memo[c] != -1:
        return memo[c]
    if c == 0:
        return 1
    result = 0
    for obj in objects:
        if obj <= c and knapsack(c - obj, objects):
            result = 1
    memo[c] = result
    return result


for test_case in range(int(input())):
    n, c = map(int, input().split())
    objects = list(map(int, input().split()))
    memo = [-1] * (c + 1)
    maxi = -1
    for cap in reversed(range(0, c + 1)):
        if knapsack(cap, objects):
            maxi = cap
            break
    print(maxi)
