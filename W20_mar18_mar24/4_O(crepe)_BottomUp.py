def ocrepe(n, k, etapes):
    dp = [[False for _ in range(k)] for _ in range(n)]

    for i in range(len(etapes[0]["ingredients"])):
        if etapes[0]["ingredients"][i] < k:
            dp[0][etapes[0]["ingredients"][i]] = True

    for i in range(1, n):
        for j in range(k):
            for ingr in etapes[i]["ingredients"]:
                if dp[i - 1][j] and ingr + j < k:
                    dp[i][ingr + j] = True

    for j in range(k - 1, 0, -1):
        if dp[n - 1][j]:
            print(j)
            return
    print(-1)


n, k = map(int, input().split())
etapes = [None] * n
for i in range(0, n):
    m = int(input())
    ingr = list(map(int, input().split()))
    etape_i = {"m": m, "ingredients": ingr}
    etapes[i] = etape_i
ocrepe(n, k, etapes)
