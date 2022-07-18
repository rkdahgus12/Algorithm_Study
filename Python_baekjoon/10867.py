import sys

input = sys.stdin.readline

soo = int(input())
res = sorted(set(list(map(int, input().split()))))
for i in res:
    print(i,end=" ")
