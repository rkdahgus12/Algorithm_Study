import sys

input = sys.stdin.readline

a, b = map(int, input().split())
res = set(map(int, (input().split())))

res1 = set(map(int, (input().split())))
list = sorted(list(res - res1))
if len(list) == 0:
    print(0)
else:
    print(len(list))
    for i in list:
        print(i, end=' ')
