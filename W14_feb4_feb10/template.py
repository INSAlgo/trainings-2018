#!/usr/bin/env python3


def kruskal(edges):
    """TODO: fill this function
    """
    tree_edges = []
    cost = 0

    return (tree_edges, cost)


def main():
    """Read the graph from the standard input, then prints the total cost
       and the edges of the MST in the order in which they were found.
    """
    m = int(input())
    edges = [(lambda s: (int(s[0]), int(s[1]), int(s[2])))(input().split())
             for _ in range(m)]
    tree, cost = kruskal(edges)
    print("\n".join("%d %d" % edge for edge in tree))
    print("---\n%d" % cost)


if __name__ == "__main__":
    main()
