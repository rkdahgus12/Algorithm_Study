from collections import Counter
import sys

input = sys.stdin.readline

soo = int(input())
res = Counter(map(int, (input().split())))
soo1 = int(input())
res1 = list(map(int, (input().split())))
for i in range(len(res1)):
    print(res[res1[i]],end=" ")
