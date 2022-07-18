import sys

input = sys.stdin.readline

res = input().rstrip()
chk = input().rstrip()

if chk in res:
    print("1")
else:
    print("0")
