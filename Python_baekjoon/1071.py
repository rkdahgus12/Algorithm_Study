import sys

input = sys.stdin.readline

soo = int(input())
res = list(map(int, input().split()))
print(res)


def swap(a1, a2):
    return a2, a1


for i in range(len(res)):
    for j in range(i,len(res)):

        if res[i] + 1 == res[j + 1]:
            res[i], res[j + 1] = swap(res[i], res[j + 1])
            break
print(res)