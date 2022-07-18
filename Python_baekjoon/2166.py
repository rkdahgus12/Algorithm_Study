import sys

input = sys.stdin.readline

soo = int(input())
bo = []
for i in range(soo):
    bo.append(list(map(int, input().split())))
print(bo)