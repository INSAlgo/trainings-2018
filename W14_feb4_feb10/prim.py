#!/usr/bin/env python3

##############################################################################
#                        Louis Sugy 2019, MIT license                        #
#                                for INSAlgo                                 #
##############################################################################

from collections import defaultdict
from heapq import heappop, heappush


def prim(edges):
    """Calculate the cost and edges of a spanning tree, given the edges of
       a graph. Complexity: O(|E| log |E|)
    """
    # Construct adjacency list - O(|E|)
    adj_list = defaultdict(list)
    for i, j, w in edges:
        adj_list[i].append((j, w))
        adj_list[j].append((i, w))
    all_nodes = list(adj_list.keys())

    # Pick a random starting node - O(1)
    start = all_nodes[0]

    # Initialize the tree's nodes and edges' data structures - O(1)
    tree_nodes = set([start])
    tree_edges = []
    cost = 0

    # Initialize the heap - O(|V|)
    hq = []
    for neighbor, w in adj_list[start]:
        heappush(hq, (w, neighbor, start))

    # Calculate the minimum spanning tree - O(|E| log |E|)
    while len(all_nodes) != len(tree_nodes):
        cost_incr, node, parent = heappop(hq)
        if node in tree_nodes:
            continue
        cost += cost_incr
        tree_nodes.add(node)
        tree_edges.append((parent, node))
        for neighbor, w in adj_list[node]:
            heappush(hq, (w, neighbor, node))

    return (tree_edges, cost)


def main():
    """Read the graph from the standard input, then prints the total cost
       and the edges of the MST in the order in which they were found.
    """
    m = int(input())
    edges = [(lambda s: (int(s[0]), int(s[1]), int(s[2])))(input().split())
             for _ in range(m)]
    tree, cost = prim(edges)
    print("\n".join("%d %d" % edge for edge in tree))
    print("---\n%d" % cost)


if __name__ == "__main__":
    main()
