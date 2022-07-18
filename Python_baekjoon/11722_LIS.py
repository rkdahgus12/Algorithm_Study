import sys
'''
6
10 30 10 20 20 10
'''
input = sys.stdin.readline

soo = int(input())
list = list(map(int, input().split()))
dp = [1] * soo
for i in range(soo):
    for j in range(i):
        if list[j] > list[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))