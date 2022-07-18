soo = int(input())
res = list(map(int, input().split()))
res.sort()
count = 0
result = 0
for i in range(len(res)):
    count += res[i]
    result += count
print(result)
