import sys

input = sys.stdin.readline

p = "IOI"
P1 = "OI"
soo = int(input())
num = int(input())
res = input().rstrip()

if soo != 1:
    p += P1 * (soo - 1)
count = 0
for i in range(len(res)):
    if i > num - len(p):
        print(count)
        break
    if res[i] == "I":
        test = ""
        for j in range(i, i + len(p)):
            test += res[j]
        if test == p:
            count += 1
