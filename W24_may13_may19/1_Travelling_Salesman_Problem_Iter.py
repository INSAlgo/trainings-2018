from collections import deque
from collections import defaultdict
# Held Karp algorithm


def extract_bit(bitmap, rank):
    return (bitmap >> rank) % 2


def put_bit(bitmap, rank, value):
    if value == 1:
        return bitmap | (1 << rank)
    else:
        return bitmap & ~(1 << rank)


def Held_Karp(graph, nodeStart):
    # for a static structure :
    mem = [[float('inf') for j in range(1 << len(graph) + 1)]
           for i in range(len(graph))]
    # mem = defaultdict(lambda: defaultdict(lambda: float('inf')))
    mem[nodeStart][1 << nodeStart] = 0
    for bitmap in range((1 << len(graph)) + 1):
        # if the path includes the first node
        if extract_bit(bitmap, 0):
            for node in range(len(graph)):
                # if the path includes the current node
                if extract_bit(bitmap, node):
                    for neighbor in graph[node]:
                        # if the path include that neighbor
                        if extract_bit(bitmap, neighbor):
                            prop = mem[neighbor][put_bit(
                                bitmap, node, 0)] + graph[node][neighbor]
                            mem[node][bitmap] = min(mem[node][bitmap], prop)

    bestDistance = float('inf')
    # find the best option with the return

    for node in range(len(graph)):
        if mem[node][(1 << len(graph))-1] != float('inf'):
            # if we can return to the starting point
            if nodeStart in graph[node]:
                candidate = mem[node][pow(
                    2, len(graph)) - 1] + graph[node][nodeStart]
                bestDistance = min(bestDistance, candidate)
    return bestDistance


# parser
for inputNumber in range(int(input())):
    sizeX, sizeY = map(int, input().split())
    nodes = list()
    nodes.append(list(map(int, input().split())))
    for nBeeper in range(int(input())):
        nodes.append(list(map(int, input().split())))
    # define the graph as list of adjacency
    graph = [dict() for k in range(len(nodes))]
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            graph[i][j] = abs(nodes[i][0]-nodes[j][0]) + \
                abs(nodes[i][1] - nodes[j][1])
            graph[j][i] = graph[i][j]
    print("The shortest path has length", Held_Karp(graph, 0))
