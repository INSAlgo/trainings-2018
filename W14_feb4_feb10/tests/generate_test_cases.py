#!/usr/bin/env python3

from math import sqrt, ceil
from random import randint, randrange, choice
from collections import defaultdict

# Associate to each test id the number of edges you want
test_cases = {
    1: 20,
    2: 50,
    3: 100,
    4: 200,
    5: 500,
    6: 1000,
    7: 2000,
    8: 5000,
    9: 10000,
    10: 20000,
    11: 50000,
    12: 100000,
    13: 200000,
    14: 500000,
    15: 1000000
}

# The weights will be chosen in the following interval:
MIN_WEIGHT, MAX_WEIGHT = 1, 20

for test_id, nb_edges in test_cases.items():
    # The maximum number of vertices is chosen accordingly
    nb_vertices = ceil(5 * sqrt(nb_edges))

    # We then construct a connected graph with nb_edges edges
    edges = []
    nodes = [0]
    neighbors = defaultdict(set)
    for _ in range(nb_edges):
        while True:
            i = choice(nodes)
            j = randrange(nb_vertices)
            if i != j and j not in neighbors[i]:
                neighbors[i].add(j)
                neighbors[j].add(i)
                nodes.append(j)
                w = randint(MIN_WEIGHT, MAX_WEIGHT)
                edges.append((min(i, j), max(i, j), w))
                break

    with open("in%0.2d.txt" % test_id, "w") as fhandler:
        fhandler.write("%d\n" % nb_edges)
        fhandler.write("".join("%d %d %d\n" % edge for edge in sorted(edges)))
