import sys

input = sys.stdin.readline
x = [0, 1, 3]
res = int(input())
for i in range(3, 1001):
    x.append((x[i - 2] * 2) + x[i - 1])
print(x[res] % 10007)
