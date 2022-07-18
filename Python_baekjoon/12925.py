from decimal import Decimal
import sys


def power(a, n):
    if n == 0:
        return 1

    x = power(a, n // 2)

    if n % 2 == 0:
        return x * x

    else:
        return x * x * a


print(power(3.15321, 700))
input = sys.stdin.readline
soo = int(input())
count = 1
while True:
    res = int(input())
    x = 3 + 5 ** (1 / 2)
    print(Decimal(power(x, res)))
    x = str(int(power(x, res)))

    if len(x[-3:]) == 2:
        print("Case #{}: 0{}".format(count, x[-3:]))
    if len(x[-3:]) == 1:
        print("Case #{}: 00{}".format(count, x[-3:]))
    elif len(x[-3:]) == 3:
        print("Case #{}: {}".format(count, x[-3:]))
    if count == soo:
        break
    count += 1
# 429
