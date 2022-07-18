import sys

input = sys.stdin.readline

res = list(str(input().rstrip()))
if list(reversed(res)) == res:
    print(1)
else:
    print(0)
