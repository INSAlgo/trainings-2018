n = int(input())
sum_diag_0 = 0
sum_diag_1 = 0
for k in range(n):
	row = list(map(int, input().split()))
	sum_diag_0 += row[k]
	sum_diag_1 += row[n-1-k]
print(abs(sum_diag_0-sum_diag_1))
