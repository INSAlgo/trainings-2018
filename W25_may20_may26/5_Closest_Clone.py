from collections import deque

n, m = map(int, input().split())
graph = [list() for k in range(n)]
for k in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)
colors = list(map(int, input().split()))
goal = int(input())
listSelect = []
# distance to the closest node that is the source of a bfs
distances = [-1 for k in range(n)]
sources = [-1 for k in range(n)]  # keep track of which BFS touched the node
for k in range(n):
    if(colors[k] == goal):
        listSelect.append(k)  # find all nodes that have the correct color
        distances[k] = 0
        sources[k] = k
res = -1
# if only one node, return:
if len(listSelect) > 1:
    # launch BFS for every starting node
    deques = [deque() for k in range(len(listSelect))]
    for k in range(len(listSelect)):
        deques[k].append(listSelect[k])

    while res == -1:
        for queue in deques:
            if queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    # if no result found, and two bfs touch each other
                    if res == -1 and distances[neighbour] != -1
                    and sources[neighbour] != sources[node]:
                        res = distances[node] + \
                            distances[neighbour] + 1  # final result
                        break
                    elif distances[neighbour] == -1:
                        distances[neighbour] = distances[node] + 1
                        sources[neighbour] = sources[node]
                        queue.append(neighbour)
print(res)
