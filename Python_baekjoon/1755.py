import sys

input = sys.stdin.readline

so1, so2 = map(int, input().split())

list = ['z', 'o', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'e', 'n']
res = []
for i in range(so1, so2):
    if 10 > i:
        res.append(list[i])
    elif 10 <= i:
        x = str(i)
        x = str(list[int(x[0])]) + str(list[int(x[1])])
        res.append(x)
res.sort()
print(list.index(res[0]))
