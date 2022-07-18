import sys

input = sys.stdin.readline

a, b = map(int, input().split())

res = list(map(int, input().split()))
res.sort()
print(res[b-1])
