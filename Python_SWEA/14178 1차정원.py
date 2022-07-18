import sys

input = sys.stdin.readline

soo = int(input().rstrip())

for i in range(soo):
    a, b = map(int, input().split())
    x = b + 1
    x = x + b
    y = x
    count = 1
    for j in range(a):
        if a <= x:
            print("#{} {}".format(i + 1, count))
            break
        x += y
        count += 1
