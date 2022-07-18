import sys
soo = int(input().rstrip())

sys.setrecursionlimit(10 ** 4)
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


for case in range(soo):
    m, n, k = map(int, (input().split()))
    graph = [[0] * m for i in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1

    print(count)
'''
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
'''
