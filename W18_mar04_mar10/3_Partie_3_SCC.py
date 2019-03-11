def dfs(node, result):
    for neigh in graph[node]:
        if not visited[neigh]:
            visited[neigh] = 1
            dfs(neigh, result)
    result.append(node)


def dfsinv(node, result):
    for neigh in graphInv[node]:
        if not visited[neigh]:
            visited[neigh] = 1
            result += dfsinv(neigh, result)
    result += 1
    return result


n, m = map(int, input().split())
graph = [list() for k in range(n)]
for k in range(m):
    i, j = map(lambda x: int(x)-1, input().split())
    graph[i].append(j)
visited = [0]*n
rDFS = list()
for k in range(n):
    if not visited[k] :
        visited[k] = 1
        dfs(k, rDFS)
visited = [0]*n
graphInv = [list() for k in range(n)]
for k in range(n):
    for neighbor in graph[k]:
        graphInv[neighbor].append(k)
rDFS = reversed(rDFS)
C = 0
D = 0
for k in rDFS:
    if not visited[k]:
        visited[k] = 1
        nb = dfsinv(k, 0)
        if nb % 2 == 0:
            D += nb
        else:
            C += nb
print(C-D)

