import sys
sys.setrecursionlimit(10000)
m, n, k = map(int, input().split())
ls = [[0] * n for i in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(y, x, count):
    ls[y][x] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= ny < m) and (0 <= nx < n) and ls[ny][nx] == 0:
            count = dfs(ny, nx, count + 1)

    return count


for i in range(k):
    res = list(map(int, input().split()))

    for a in range(res[1], res[3]):
        for b in range(res[0], res[2]):
            ls[a][b] = True

cores = []
for a in range(m):
    for b in range(n):
        if ls[a][b] == 0:
            cores.append(dfs(a, b, 1))
cores.sort()
print(len(cores))
print(*cores,end=' ')