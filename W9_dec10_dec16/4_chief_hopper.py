#!/bin/python3


def chiefHopper(arr):
    sumh = 0
    minE = 0
    p2 = 1
    for val in arr:
        sumh = 2 * sumh + val
        p2 *= 2

        # this is ugly but ceil() has numerical instability
        neededE = sumh // p2
        if sumh % p2:
            neededE += 1

        if neededE > minE:
            minE = neededE
    return minE


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)
    print(result)
