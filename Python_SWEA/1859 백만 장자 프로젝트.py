soo = int(input().rstrip())

for i in range(soo):
    ca = int(input())
    res = list(map(int, input().split()))
    ma = res[-1]
    count = 0
    for k in range(ca - 2, -1, -1):
        if res[k] >= ma:
            ma = res[k]
        else:
            count += ma - res[k]
    print("#{} {}".format(i + 1, count))
