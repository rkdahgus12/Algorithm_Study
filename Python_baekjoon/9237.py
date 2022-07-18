import sys

input = sys.stdin.readline
n = int(input())
res = list(map(int, input().split()))
res.sort(reverse=True)
for i in range(len(res)):
    res[i] = res[i] + i + 1
print(max(res) + 1)
