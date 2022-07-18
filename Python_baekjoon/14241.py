import sys

input = sys.stdin.readline
soo = int(input())
res = list(map(int, input().split()))
res.sort(reverse=True)
# sum
count = res[0]
# score
res_sum = 0
for i in range(1, len(res)):
    res_sum += count * res[i]
    count += res[i]

print(res_sum)
