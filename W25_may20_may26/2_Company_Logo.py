from collections import defaultdict
s = input()
d = defaultdict(lambda: 0)
for k in s:
    d[k] += 1
res = sorted(d.keys())
res = sorted(res, key=lambda x: -d[x])
for k in range(3):
    print(res[k], d[res[k]])
