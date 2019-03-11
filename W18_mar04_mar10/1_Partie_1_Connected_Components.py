from collections import deque
n = int(input())
visited = [0]*2*n
graph = [list() for k in range(2*n)]
for k in range(n):
    i, j = map(lambda x: int(x)-1, input().split())
    graph[i].append(j)
    graph[j].append(i)
minSize = 2*n
maxSize = 1
queue = deque()
for k in range(2*n):
    if not visited[k]:
        # BFS
        nb_nodes = 0
        queue.append(k)
        visited[k] = 1
        while queue:
            nb_nodes += 1
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = 1
        if nb_nodes != 1:
            minSize = min(minSize, nb_nodes)
        maxSize = max(maxSize, nb_nodes)
print(minSize, maxSize)
