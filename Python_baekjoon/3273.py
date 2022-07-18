import sys

input = sys.stdin.readline

soo = int(input())
res = list(map(int, (input().split())))
res.sort()

chk = int(input())
count = 0
i = 0
while True:
    if len(res) == 2:
        if res[0] + res[1] == chk:
            count = 1
            break
        else:
            count = 0
        break
    if i >= len(res):
        break
    if chk - res[0] in res:
        count += 1
        res.remove(chk - res[0])
        res.remove((res[0]))
    i += 1

print(count)
