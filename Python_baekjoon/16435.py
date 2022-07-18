# testCase
'''
3 10
10 11 13
'''
import sys

input = sys.stdin.readline
f, lo = map(int, input().split())
res = list(map(int, (input().split())))
res.sort()
for i in res:
    if lo >= i:
        lo += 1
print(lo)
