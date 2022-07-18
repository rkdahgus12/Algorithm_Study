res = [i for i in input()]
res.sort(reverse=True)
print(res)
sum = 0
for i in res:
    sum += int(i)
if sum % 3 != 0 or "0" not in res:
    print(-1)
else:
    print(''.join(res))
