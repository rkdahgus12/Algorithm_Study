import sys
from collections import Counter

input = sys.stdin.readline

le = int(input())
res = Counter(input())
if res[res.most_common()[0][0]] == 1:
    print(0)
else:
    print(res[res.most_common()[0][0]])
