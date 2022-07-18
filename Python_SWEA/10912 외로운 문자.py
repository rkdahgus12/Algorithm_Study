for case in range(1, int(input()) + 1):
    res = list(input())
    res.sort()
    for i in range(1, len(res)):
        if res[i - 1] == res[i]:
            res[i - 1], res[i] = 0, 0
    res = list(set(res))

    if res[0] == 0 and len(res) == 1:
        print("#{} Good".format(case))
    else:
        st = ""
        for k in res:
            if k == 0:
                continue
            else:
                st += k

        print("#{} {}".format(case, st))
