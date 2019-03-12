n, k = map(int, input().split())
numbers = sorted((map(int, input().split())))  # remove duplicate
cpt = 0
for a in range(n):
    for b in range(a+1, n):
        if (numbers[a]+numbers[b]) % k == 0:
            cpt += 1
print(cpt)
