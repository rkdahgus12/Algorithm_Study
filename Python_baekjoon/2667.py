# n = int(input())
# graph = []
# num = []
#
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def DFS(x, y):
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#
#     if graph[x][y] == 1:
#         global count
#         count += 1
#         graph[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             DFS(nx, ny)
#         return True
#     return False
#
#
# count = 0
# result = 0
#
# for i in range(n):
#     for j in range(n):
#         if DFS(i, j) == True:
#             num.append(count)
#             result += 1
#             count = 0
#
# num.sort()
# print(result)
# for i in range(len(num)):
#     print(num[i])
soo = int(input().rstrip())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= soo or y < 0 or y >= soo:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
result = 0
num = []
for i in range(soo):
    graph.append(list(map(int, input())))
for i in range(soo):
    for j in range(soo):
        if dfs(i, j) == True:
            num.append(count)
            result += 1
            count = 0
print(result)
num.sort()
for i in range(len(num)):
    print(num[i])
