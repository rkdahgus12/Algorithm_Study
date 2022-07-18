import sys

input = sys.stdin.readline

a, b = map(int, input().split())
res = []
for i in range(1, a + 1):
    res.append(i)
i = 0
re = ""
while True:

    if i == b - 1:
        chk = res.pop(0)
        re+=str(chk)
        i = 0
    if len(res) == 0:
        break
    res.append(res.pop(0))
    i += 1
print("<", ', '.join(re), ">", sep = '')
