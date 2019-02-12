#!/bin/python3

import os
import sys
from collections import defaultdict
from heapq import heappush, heappop

INF = 1000000000000


def shortestReach(n, adj_lists, s):
    # Finding the shortest path
    parent = {}
    costs = {}
    hq = [(0, s, s)]
    while hq:
        e_cost, p, elem = heappop(hq)
        if elem in costs:
            continue
        costs[elem] = e_cost
        parent[elem] = p
        for child, w in adj_lists[elem].items():
            if child not in costs:
                heappush(hq, (e_cost + w, elem, child))

    # Calculating the result
    return [costs[i] if i in costs else -1
            for i in range(1, n + 1)
            if i != s]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(sys.stdin.readline().rstrip())

    for t_itr in range(t):
        nm = sys.stdin.readline().rstrip().split()

        n = int(nm[0])
        m = int(nm[1])

        adj_lists = defaultdict(lambda: defaultdict(lambda: INF))
        for _ in range(m):
            i, j, w = map(int, sys.stdin.readline().rstrip().split())
            adj_lists[i][j] = min(adj_lists[i][j], w)
            adj_lists[j][i] = min(adj_lists[j][i], w)

        s = int(input())

        result = shortestReach(n, adj_lists, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
