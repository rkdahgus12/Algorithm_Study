import sys

input = sys.stdin.readline
soo = int(input())
count = 0
if soo == 1:
    print(1)
else:
    for i in range(1, soo + 1):
        count += i
        if count > soo:
            print(i - 1)
            break
