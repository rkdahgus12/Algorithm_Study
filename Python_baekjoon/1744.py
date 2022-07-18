import sys

input = sys.stdin.readline

soo = int(input())
res = []
for i in range(soo):
    res.append(int(input()))
res.sort(reverse=True)
count = 0
j=0
for i in range(soo):
    if res[i-1] > 0 and i%2==1:
        count += res[i-1] * res[i]
