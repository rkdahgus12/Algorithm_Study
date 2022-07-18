import sys
input=sys.stdin.readline
n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(input()))

chk = min(n, m)
res = 0
for i in range(n):
    for j in range(m):
        for k in range(chk):
            if ((i + k) < n) and ((j + k) < m) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                res = max(res, (k + 1) ** 2)

print(res)