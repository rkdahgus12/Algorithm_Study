import sys

input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    res.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            res[i][j] = res[i][j] + res[i - 1][j]
        elif i == j:
            res[i][j] = res[i][j] + res[i - 1][j - 1]
        else:
            res[i][j] = max(res[i - 1][j - 1], res[i - 1][j]) + res[i][j]
    k += 1
print(max(res[n - 1]))

