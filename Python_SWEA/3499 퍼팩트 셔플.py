soo = int(input().rstrip())
for i in range(soo):
    cas = int(input())
    res = list(map(str, input().split()))
    if cas % 2 == 0:
        compare = res[cas // 2:]
        del res[cas // 2:]
    else:
        compare = res[cas // 2 + 1:]
        del res[cas // 2 + 1:]

    if len(res) == len(compare):
        st = ""
        for z1, z2 in zip(res, compare):
            st += z1 + " " + z2 + " "
        print("#{} {}".format(i + 1, st))
    else:
        st = res[0] + " "
        del res[0]
        for z1, z2 in zip(res, compare):
            st += z2 + " " + z1 + " "
        print("#{} {}".format(i + 1, st))
