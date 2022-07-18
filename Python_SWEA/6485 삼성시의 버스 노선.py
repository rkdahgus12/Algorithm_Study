for case in range(1, int(input()) + 1):
    soo = int(input())
    res = []
    ls = [0] * 5000
    for i in range(soo):
        res.append(list(map(int, input().split())))
    for j in res:
        for k in range(j[0] - 1, j[1]):
            ls[k] += 1

    p = int(input())
    st = ""
    for k in range(p):
        chk = int(input())
        st += " " + str(ls[chk - 1])
    print("#{}{}".format(case, st))
