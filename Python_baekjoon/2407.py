import sys

input = sys.stdin.readline

a, b = map(int, input().split())
res = 1
count = 1
for i in range(a, a - b, -1):
    count *= i
for i in range(1, b + 1):
    res *= i
print(count // res)
