t = int(input().rstrip())

for tc in range(1, t + 1) :
    n, d = map(int, input().split())
    d = d * 2 + 1
    result = n // d
    if n % d != 0 :
        result += 1

    print('#%d %d' % (tc, result))