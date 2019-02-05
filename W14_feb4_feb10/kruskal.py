#!/usr/bin/env python3

##############################################################################
#                        Louis Sugy 2019, MIT license                        #
#                                for INSAlgo                                 #
##############################################################################

from heapq import heappop, heappush
from unionfind import UnionFind


def kruskal(edges):
    """Calculate the cost and edges of a spanning tree, given the edges of
       a graph. Complexity: O(|E| log |E|)
    """
    # Find all the nodes and create a heap of edges - O(|E|)
    all_nodes = set()
    hq = []
    for i, j, w in edges:
        all_nodes.add(i)
        all_nodes.add(j)
        heappush(hq, (w, i, j))

    # Initialize the forest - O(|V|)
    forest = UnionFind(all_nodes)

    # Initialize the tree's data structure - O(1)
    tree_edges = []
    cost = 0

    # Calculate the minimum spanning tree - O(|E| log |E|)
    while hq:
        cost_incr, n1, n2 = heappop(hq)
        if forest.is_same_set(n1, n2):
            continue
        cost += cost_incr
        forest.union(n1, n2)
        tree_edges.append((n1, n2))

    return (tree_edges, cost)


def main():
    """Read the graph from the standard input, then prints the total cost
       and the edges of the MST in the order in which they were found.
    """
    m = int(input())
    edges = [(lambda s: (int(s[0]), int(s[1]), int(s[2])))(input().split())
             for _ in range(m)]
    tree, cost = kruskal(edges)
    print(cost)
    print("\n".join("%d %d" % edge for edge in tree))


if __name__ == "__main__":
    main()
