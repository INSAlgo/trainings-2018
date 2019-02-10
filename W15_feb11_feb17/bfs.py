#!/usr/bin/env python3
from collections import defaultdict, deque


def bfs(edges, start, end):
    """Finds the shortest path between start and end in the graph which edges
       are given. Returns the order of the nodes in that path.
    """
    # Constructing adjacency lists
    adj_lists = defaultdict(list)
    for i, j in edges:
        adj_lists[i].append(j)
        adj_lists[j].append(i)

    # Finding the shortest path
    parent = {start: start}
    dq = deque([start])
    while dq:
        elem = dq.popleft()
        for child in adj_lists[elem]:
            if child not in parent:
                parent[child] = elem
                dq.append(child)

    # Calculating the result
    path_nodes = [end]
    current = end
    while parent[current] != current:
        path_nodes.append(parent[current])
        current = parent[current]
    path_nodes.reverse()

    return path_nodes


def main():
    """Read the graph from the standard input, then prints the total cost
       and the edges of the shortest path.
    """
    m = int(input())
    start, end = map(int, input().split())
    edges = [(lambda s: (int(s[0]), int(s[1])))(input().split())
             for _ in range(m)]
    path_nodes = bfs(edges, start, end)
    cost = len(path_nodes) - 1
    print(" ".join(map(str, path_nodes)))
    print("---\n%d" % cost)


if __name__ == "__main__":
    main()
