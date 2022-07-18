n, m = map(int, (input().split()))
# 세로로 list 입력받을 때
nums = [int(input()) for i in range(n)]
k = len(nums)-1
count = 0
while True:
    if m==0:
        break
    if nums[k] <= m:
        count += m // nums[k]
        m -= nums[k] * (m // nums[k])
    elif nums[k] > m:
        k -= 1
print(count)