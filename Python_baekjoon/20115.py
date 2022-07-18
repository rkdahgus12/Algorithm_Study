# import sys
#
# input = sys.stdin.readline
#
# soo = int(input())
#
# res = list(map(int, input().split()))
# ma = max(res)
# res.remove(max(res))
# j = 0
# for i in range(len(res) - j):
#     ma += min(res) / 2
#     res.remove(min(res))
#     j += 1
# print(ma)
import sys

input = sys.stdin.readline

soo = int(input())

res = list(map(int, input().split()))
res.sort(reverse=True)
ma=res[0]
for i in res:
    if i==ma:
        continue
    ma+=i/2
print(ma)