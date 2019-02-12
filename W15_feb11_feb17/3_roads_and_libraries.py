#!/bin/python3

import os


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib
    forest = UnionFind(range(1, n + 1))
    for i, j in cities:
        forest.union(i, j)
    roots = set()
    for i in range(1, n + 1):
        roots.add(forest.find(i))
    nb_cc = len(roots)
    return nb_cc * c_lib + (n - nb_cc) * c_road


class UnionFind:
    def __init__(self, singletons):

        self.parents = {e: e for e in singletons}
        self.rank = {e: 0 for e in singletons}

    def find(self, e):
        if e not in self.parents:
            return None
        if self.parents[e] != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1, e2):
        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:
            return
        if self.rank[r1] < self.rank[r2]:
            r1, r2 = r2, r1
        self.parents[r2] = r1
        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1

    def is_same_set(self, e1, e2):
        return (self.find(e1) == self.find(e2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
