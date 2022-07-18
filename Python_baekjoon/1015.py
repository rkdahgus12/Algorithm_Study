import sys
from collections import Counter
input = sys.stdin.readline

soo = int(input())
res = []
for i in range(soo):
    res.append(input().rstrip())
res.sort()
print(Counter(res).most_common()[0][0])
