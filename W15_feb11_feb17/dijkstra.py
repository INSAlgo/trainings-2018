#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(edges, start, end):
    """Finds the shortest path between start and end in the graph which edges
       are given. Returns the order of the nodes in that path.
    """
    # Constructing adjacency lists
    adj_lists = defaultdict(list)
    for i, j, w in edges:
        adj_lists[i].append((j, w))
        adj_lists[j].append((i, w))

    # Finding the shortest path
    parent = {}
    costs = {}
    hq = [(0, start, start)]
    while hq:
        e_cost, p, elem = heappop(hq)
        if elem in costs:
            continue
        costs[elem] = e_cost
        parent[elem] = p
        for child, w in adj_lists[elem]:
            if child not in costs:
                heappush(hq, (e_cost + w, elem, child))

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
    path_nodes, cost = dijkstra(edges, start, end)
    print(" ".join(map(str, path_nodes)))
    print("---\n%d" % cost)


if __name__ == "__main__":
    main()
