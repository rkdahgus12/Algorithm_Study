soo = int(input())
st = ""
res = []
for i in range(1, soo + 1):
    k = str(i)
    if k.count('3') or k.count('6') or k.count('9'):
        x = k.count('3') + k.count('6') + k.count('9')
        k = '-' * x
    res.append(k)

print(' '.join(res))
