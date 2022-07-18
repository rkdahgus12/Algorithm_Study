import sys

input = sys.stdin.readline
soo = int(input())
res = []
for i in range(soo):
    res.append(int(input()))
res.sort(reverse=True)
for i in range(soo):
    res[i]*=i+1
print(max(res))
