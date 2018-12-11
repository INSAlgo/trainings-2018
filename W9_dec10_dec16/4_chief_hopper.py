#!/bin/python3


def chiefHopper(arr):
    x = 0
    for val in arr[::-1]:
        x = (x + val + 1) // 2
    return x


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)
    print(result)
