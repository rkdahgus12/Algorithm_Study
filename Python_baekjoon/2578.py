import sys

input = sys.stdin.readline

res = []
vi = [[True] * 5] * 5

print()
for i in range(5):
    a = list(map(int, input().split()))
    res.append(a)
print(res)
