import sys


def GCD(x, y):
    while (y):
        x, y = y, x % y
    return x


def solve(a1, a2):
    result = (a1 * a2) // GCD(a1, a2)
    return result


input = sys.stdin.readline
soo = int(input())
for _ in range(soo):
    a1, a2 = map(int, input().split())
    print(solve(a1, a2))
