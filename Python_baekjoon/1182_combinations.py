from itertools import combinations
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
res = list(map(int, input().split()))

com = []
for i in range(a + 1):
    com = com + list(combinations(res, i))
count=0
for i in range(1,len(com)):
    if sum(com[i])==b:
        count+=1

print(count)
