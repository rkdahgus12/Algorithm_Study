import sys
from collections import Counter
soo = int(sys.stdin.readline())
ls = []
for i in range(soo):
    inp = int(sys.stdin.readline())
    ls.append(inp)
ls.sort()
print(round(sum(ls) / soo))  # 합 (1)
if soo == 1:
    print(ls[0])
else:
    print(ls[soo // 2])  # 중앙 값 (2)
count_ls = []
max_soo = 0
max_num = -0
counting = 0
count = Counter(ls).most_common()
if len(count) > 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])
print(max(ls) - min(ls))
