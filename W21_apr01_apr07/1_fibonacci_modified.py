t1, t2, n = map(int, input().split())
mem = [[0 for k in range(2)] for i in range(n + 1)]
mem[1][0] = t1
mem[2][0] = t2
mem[1][1] = t1 * t1
mem[2][1] = t2 * t2
for k in range(3, n + 1):
    mem[k][0] = mem[k - 2][0] + mem[k - 1][1]
    mem[k][1] = mem[k][0] * mem[k][0]
print(mem[n][0])
