n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
tot = 0
for k in range(n):
    if arr[k] in A:
        tot += 1
    elif arr[k] in B:
        tot -= 1
print(tot)
