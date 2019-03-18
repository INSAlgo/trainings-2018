def ocrepe(n, k, steps):
    dp = [[False for _ in range(k)] for _ in range(n)]

    for i in range(len(steps[0]["ingredients"])):
        if steps[0]["ingredients"][i] < k:
            dp[0][steps[0]["ingredients"][i]] = True

    for i in range(1, n):
        for j in range(k):
            for ingr in steps[i]["ingredients"]:
                if dp[i - 1][j] and ingr + j < k:
                    dp[i][ingr + j] = True

    for j in range(k - 1, 0, -1):
        if dp[n - 1][j]:
            print(j)
            return
    print(-1)


n, k = map(int, input().split())
steps = [None] * n
for i in range(0, n):
    m = int(input())
    ingr = list(map(int, input().split()))
    step_i = {"m": m, "ingredients": ingr}
    steps[i] = step_i
ocrepe(n, k, steps)
