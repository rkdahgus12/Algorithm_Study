from collections import Counter
import sys

input = sys.stdin.readline
soo = int(input())
res=""
for i in range(soo):
    res+=input().rstrip()
print(Counter(res).most_common(1)[0][0])