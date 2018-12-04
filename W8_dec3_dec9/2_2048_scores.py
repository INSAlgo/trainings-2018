memo = {0: (0, 0), 2: (0, 1)}


def calc_rec(n):
    global memo
    if n in memo:
        return memo[n]
    else:
        score, turns = calc_rec(n // 2)
        memo[n] = (2 * score + n, 2 * turns)
        return memo[n]


numbers = []
for _ in range(4):
    for i in input().split():
        numbers.append(int(i))
fours = int(input())

tscore, tturns = 0, 0
for nb in numbers:
    s, t = calc_rec(nb)
    tscore += s
    tturns += t

tturns -= fours + 2
tscore -= 4 * fours

print(tscore)
print(tturns)
