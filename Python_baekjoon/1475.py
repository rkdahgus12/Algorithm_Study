import sys


soo = input()
res = [0] * 10
count = 0
for i in soo:
    if i == '6' or i == '9':
        count += 1
    else:
        res[int(i)] += 1
if count % 2 == 0:
    count //= 2
else:
    count = count // 2 + 1
res[6]=count
print(max(res))
