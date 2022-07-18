import sys
input=sys.stdin.readline
soo = int(input())

A = list(map(int, input().split()))

res = [1] * soo

for i in range(soo):
    for j in range(i):
        if A[j] < A[i]:
            res[i] = max(res[i], res[j] + 1)

print(max(res))
