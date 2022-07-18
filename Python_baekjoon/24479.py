n, m, r = map(int, input().split())
visited = [False] * (n + 1)


def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for j in range(1, n + 1):
    if len(graph[j]) == 0:
        graph[j].append('0')
    graph[j].sort()
print(graph)
dfs(r)
