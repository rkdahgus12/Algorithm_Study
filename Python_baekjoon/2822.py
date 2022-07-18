import sys

input = sys.stdin.readline
res_dict = {}
for i in range(8):
    var = i + 1
    key = int(input())
    res_dict[key] = var
res1 = sorted(res_dict, reverse=True)
res2 = sorted(res_dict.items(), reverse=True)
list = []
for i in range(5):
    list.append(res2[i][1])
list.sort()
print(sum(res1[:5]))
for i in range(5):
    print(list[i],end=" ")