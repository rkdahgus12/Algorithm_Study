import sys

input = sys.stdin.readline

a, b = map(int, input().split())

res = set()
for i in range(a):
    res.add(input().rstrip())
res1 = set()
for i in range(b):
    res1.add(input().rstrip())
print(res & res1)
list = sorted(list(res & res1))
print(len(list), sep="\n")
for i in list:
    print(i)
