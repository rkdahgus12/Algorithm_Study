import sys

input = sys.stdin.readline

a, b = map(int, input().split())
count = 0
res = [soo for soo in range(2, a + 1)]

for j in range(len(res)):
    chk = res[0]
    for i in range(len(res)):
        if len(res) <= i:
            break
        if res[i] % chk == 0:
            chk2 = res.pop(i)
            count += 1
        if count == b:
            break
        if len(res) <= i:
            break
        elif res[i] % chk != 0 or res[i] == None:
            continue

    if count == b:
        print(chk2)
        break
