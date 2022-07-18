import sys

input = sys.stdin.readline

soo = int(input())
res = []
for i in range(soo):
    a = int(input())
    res.append(a)
res.sort(reverse=True)
for i in res:
    print(i)
