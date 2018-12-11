#!/bin/python3


def getMinimumCost(k, c):
    cs = sorted(c, reverse=True)
    cost = 0
    for i in range(len(cs)):
        cost += cs[i] * (i // k + 1)

    return cost


if __name__ == '__main__':
    n, k = map(int, input().split())
    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
