from collections import defaultdict

from math import ceil


def main():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    _, max_path = tree_descent_rec(graph, None, list(graph.keys())[0])
    print(int(ceil(max_path / 2)))


def tree_descent_rec(graph, parent, node):
    child_res = []
    for child in graph[node]:
        if child != parent:
            child_res.append(tree_descent_rec(graph, node, child))
    if not child_res:
        return (1, 0)
    depth = max(res[0] for res in child_res) + 1
    if len(child_res) > 1:
        max1 = max(child_res[0][0], child_res[1][0])
        max2 = min(child_res[0][0], child_res[1][0])
        for res in child_res[2:]:
            if res[0] > max1:
                max2 = max1
                max1 = res[0]
            elif res[0] > max2:
                max2 = res[0]
        max_incl = max1 + max2
    else:
        max_incl = 0
    max_path = max(max(res[1] for res in child_res), max_incl, depth)
    return (depth, max_path)


main()
