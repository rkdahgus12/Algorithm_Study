import sys

input = sys.stdin.readline

soo = int(input())
count = 0
res = [soo for soo in range(91)]
for i in range(2, len(res)):
    res[i] = res[i - 1] + res[i - 2]
print(res[soo])