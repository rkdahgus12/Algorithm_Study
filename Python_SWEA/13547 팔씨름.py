soo = int(input().rstrip())

for i in range(soo):
    res = list(map(str, input()))
    if 15 - res.count('x') <= 7:
        print("#{} NO".format(i + 1))

    else:
        print("#{} YES".format(i + 1))
