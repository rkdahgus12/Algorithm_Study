import sys

input = sys.stdin.readline

soo = int(input())
sta = list(map(int, input().split()))
print(sta)
chk = sta.pop(0)
res = []
flag=False
for i in range(soo):
    if flag==True:

    if chk < sta[i]:
        res.append(sta[i])
        flag=True
    elif chk >= sta[i]:
        continue
    else:
        print(-1)
