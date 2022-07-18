import math
import sys
input=sys.stdin.readline
x, y = map(int, input().split())

print(math.trunc(x + y + (min(x, y) / 10)))  # trunc == 버림
