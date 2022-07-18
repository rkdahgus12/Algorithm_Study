import sys

input = sys.stdin.readline

soo = int(input())
res = list(map(int, input().split()))
res.sort()
point = 1
for i in res:
    if point < i:
        break
    point += i
print(point)
