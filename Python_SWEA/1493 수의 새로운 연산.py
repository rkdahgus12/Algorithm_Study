for case in range(int(input())):
    a, b = map(int, input().split())
    res = [[0] * 300 for i in range(300)]
    res[1][1] = 1
    xy = []
    for i in range(2, len(res)):
        res[i][1] = res[i - 1][1] + i - 1
    if a == 1:
        xy.append(1)
        xy.append(1)
    elif b == 1:
        xy.append(1)
        xy.append(1)
    count = 0
    for j in range(1, len(res)):
        for i in range(1, len(res)):
            if j == 1 and i == 1:
                continue
            elif j == 1 and i != 1:
                res[j][i] = res[j][i - 1] + i + count

            elif i > 1:
                res[j][i] = res[j][i - 1] + i + count
            if a == res[j][i]:
                xy.append(j)
                xy.append(i)

            if b == res[j][i]:
                xy.append(j)
                xy.append(i)

        count += 1

    if a == 1 and b == 1:
        print("#{} {}".format(case + 1, res[2][2]))



    else:
        print("#{} {}".format(case + 1, res[xy[0] + xy[2]][xy[1] + xy[3]]))
