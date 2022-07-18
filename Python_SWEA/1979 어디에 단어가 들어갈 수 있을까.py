soo = int(input().rstrip())


def dis(res, k):
    sta = 0
    for zz1 in range(n):
        count = 0
        for zz2 in range(n):
            if res[zz2][zz1] == 0:
                if count == k:
                    sta += 1
                    count = 0
                else:
                    count = 0
            elif res[zz2][zz1] == 1:
                count += 1
        if count == k:
            sta += 1

    return sta


for i in range(soo):
    n, k = map(int, input().split())
    res = []
    for j in range(n):
        ls = list(map(int, input().split()))
        res.append(ls)

    sta = 0

    for zz1 in range(n):
        count = 0
        for zz2 in range(n):
            if res[zz1][zz2] == 0:
                if count == k:
                    sta += 1
                    count = 0
                else:
                    count = 0
            elif res[zz1][zz2] == 1:
                count += 1
        if count == k:
            sta += 1
    sta += dis(res, k)
    print("#{} {}".format(i + 1, sta))
