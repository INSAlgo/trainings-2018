n = int(input())
bills = [20, 10, 5, 1]
nbill = []

for bill in bills:
    nbill.append(n // bill)
    n -= nbill[-1] * bill

print(" + ".join("%d*%d$" % (nbill[i], bills[i])
                 for i in range(len(bills))))
