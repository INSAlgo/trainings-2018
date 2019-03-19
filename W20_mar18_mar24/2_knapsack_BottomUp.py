for test_case in range(int(input())):
    n, c = map(int, input().split())
    objects = list(map(int, input().split()))
    dp = [0] * (c + 1)
    dp[0] = 1
    maxi = 0
    for i in range(c + 1):
        for obj in objects:
            if obj <= i:
                if dp[i - obj]:
                    dp[i] = 1
                    maxi = i
    print(maxi)
