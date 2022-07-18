import sys

input = sys.stdin.readline
soo = int(input())
res = []
for i in range(soo):
    var = int(input())
    res.append(var)
res.sort(reverse=True)
print(res)
count = 0
sum = 0
for i in range(soo):
    count += 1
    if count % 3 == 0:
        continue
    sum += res[i]
print(sum)
