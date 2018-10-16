l = list(map(int, input().split()))
avg = 0
for i in l:
    avg += int(i)
avg /= len(l)
print("{:.10f}".format(avg))
