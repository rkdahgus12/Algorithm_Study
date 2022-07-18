import sys

input = sys.stdin.readline

soo = int(input())
res = list(map(int, input().split()))
res.sort()

le = len(res) // 2

if len(res) % 2 == 0 and len(res) >= 3:
    print(res[le - 1])
elif len(res) % 2 == 1 and len(res) >= 3:
    print(res[le])
elif len(res) <= 2:
    print(max(res))
else:
    print(res[0])
