from collections import deque

q = deque([(0, 0)])
n, m, r = map(int, input().split())
graph = [[] * n for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a]
