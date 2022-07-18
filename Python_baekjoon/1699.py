import sys
import math

input = sys.stdin.readline

soo = int(input())


def sol(a1):
    return int(math.sqrt(a1)) ** 2


1
count = 0
while True:
    if soo == 0:
        break
    soo -= sol(soo)
    count += 1
print(count)
