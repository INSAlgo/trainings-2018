n = int(input())
p = list(map(int,input().split()))
antecedent = [0] * n
for k in range(n):
    antecedent[p[p[k] - 1] - 1] = k
    # store wich integer has k as the result of the composition
for k in antecedent:
    print(k + 1)
