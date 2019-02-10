#!/usr/bin/env python3
from collections import defaultdict

INF = 10000000000


def bellman_ford(edges, start, end):
    """Finds the shortest path between start and end in the graph which edges
       are given. Returns the order of the nodes in that path.
    """
    # We need to know the nodes
    vertices = set()
    for i, j, w in edges:
        vertices.add(i)
        vertices.add(j)

    # Initialization
    costs = defaultdict(lambda: INF)
    parent = defaultdict(lambda: None)
    costs[start] = 0
    parent[start] = start

    # Relax edges repeatedly
    for _ in range(len(vertices)):
        for i, j, w in edges:
            if costs[i] + w < costs[j]:
                costs[j] = costs[i] + w
                parent[j] = i

    # Check for negative-weight cycles
    for i, j, w in edges:
        if costs[i] + w < costs[j]:
            return None, None

    # Calculating the result
    path_nodes = [end]
    current = end
    while parent[current] != current:
        path_nodes.append(parent[current])
        current = parent[current]
    path_nodes.reverse()

    return (path_nodes, costs[end])


def main():
    """Read the graph from the standard input, then prints the total cost
       and the edges of the shortest path.
    """
    m = int(input())
    start, end = map(int, input().split())
    edges = [(lambda s: (int(s[0]), int(s[1]), int(s[2])))(input().split())
             for _ in range(m)]
    path_nodes, cost = bellman_ford(edges, start, end)
    if cost is None:
        print("the graph contains negative-weight cycles")
    else:
        print(" ".join(map(str, path_nodes)))
        print("---\n%d" % cost)


if __name__ == "__main__":
    main()
