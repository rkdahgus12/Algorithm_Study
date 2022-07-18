soo = int(input().rstrip())

for i in range(soo):
    a, b, c, d = map(int, input().split())
    if b < c:
        print("#{} {}".format(i + 1, 0))

    elif b >= c and b < d:
        x = abs(abs(a - c) - b)
        print("#{} {}".format(i + 1, x))
    elif b >= c and b > d:
        x = abs(abs(a - c) - d)
        print("#{} {}".format(i + 1, x))
    elif a == b == c == d:
        print("#{} {}".format(i + 1, 0))

