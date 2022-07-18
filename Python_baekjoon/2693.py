import sys

input = sys.stdin.readline

soo = int(input())
while soo >= 1:
    res = list(map(int, input().split()))
    res.sort(reverse=True)
    print(res[2])
    soo-=1

