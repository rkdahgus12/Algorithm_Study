import sys

input = sys.stdin.readline

soo = int(input())
for i in range(soo):
    res = list(input().rstrip())
    chk = res[len(res) - 1]
    test = []
    for j in range(len(res) - 2, 0, -1):
        if chk > res[j]:
            res[len(res) - 1], res[j] = res[j], res[len(res) - 1]
            test.append("".join(res))
            chk=res[j]
# for j in range(len(res) - 2, 0, -1):
#     for k in range(len(res) - 2, 0, -1):
#         if res[j]<res[k]:
