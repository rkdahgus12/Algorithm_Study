import sys

input = sys.stdin.readline
soo1 = int(input())
res1 = set(map(int, input().split()))
soo2 = int(input())
res2 = list(map(int, input().split()))
for i in range(soo2):
    if res2[i] in res1:
        print(1)
    else:
        print(0)
