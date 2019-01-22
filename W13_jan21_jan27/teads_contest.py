from collections import defaultdict

from math import ceil


def main():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    seen = set()
    _, max_path = tree_descent_rec(graph, seen, list(graph.keys())[0])
    print(int(ceil(max_path / 2)))


def tree_descent_rec(graph, seen, node):
    seen.add(node)
    child_res = []
    for child in graph[node]:
        if child not in seen:
            child_res.append(tree_descent_rec(graph, seen, child))
    if not child_res:
        return (1, 0)
    depth = max(res[0] for res in child_res) + 1
    max_incl = (sum(sorted((res[0] for res in child_res), reverse=True)[:2])
                if len(child_res) > 1 else 0)
    max_path = max(max(res[1] for res in child_res), max_incl, depth)
    return (depth, max_path)


main()
