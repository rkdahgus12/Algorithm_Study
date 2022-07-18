import sys

input = sys.stdin.readline

soo = input().rstrip()
res = []
for i in range(len(soo)):
    res.append(soo[i:])
res.sort()
for i in res:
    print(i)
