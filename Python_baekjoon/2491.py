import sys

input = sys.stdin.readline

soo = int(input())
res = list(map(int, (input().split())))
dp1, dp2 = [1]*soo, [1]*soo
for i in range(1, soo):
    if res[i] <= res[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if res[i] >= res[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(max(max(dp1), max(dp2)))
