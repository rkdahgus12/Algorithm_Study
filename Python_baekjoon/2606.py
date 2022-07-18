n = int(input())
m = int(input())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n + 1)


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
#
# BFS
# import sys
# from collections import deque
#
# # N: 노드 수 / M: 엣지 수
# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
#
# # 인접 리스트
# adj = [[] for _ in range(N)]
# visited = [0 for _ in range(N)]
#
# # 인접 리스트 채우기
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split(" "))
#     adj[x-1].append(y-1)
#     adj[y-1].append(x-1)
#
# queue = deque()
# queue.append(0)  # 1번 컴퓨터
# visited[0] = 1
# count = 0
#
# # bfs
# while queue:
#     v = queue.popleft()
#     count += 1
#
#     # v와 인접한 모든 애들
#     for each in adj[v]:
#         if visited[each] == 0:
#             queue.append(each)
#             visited[each] = 1
#
# print(count-1)