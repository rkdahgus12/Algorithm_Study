soo = int(input().rstrip())

for i in range(soo):
    res = []
    for j in range(9):
        push = list(map(int, input().split()))
        res.append(push)

    for j in range(9):
        rr = []
        for k in range(9):
            rr.append(res[k][j])
        res.append(rr)
    rr = []
    for ii in range(9):

        for jj in range(3):
            if len(rr) == 9:
                res.append(rr)
                rr = []
            rr.append(res[ii][jj])
    rr = []
    for ii in range(9):
        for jj in range(3, 6):
            if len(rr) == 9:
                res.append(rr)
                rr = []
            rr.append(res[ii][jj])
    rr = []
    for ii in range(9):
        for jj in range(6, 9):
            if len(rr) == 9:
                res.append(rr)
                rr = []
            rr.append(res[ii][jj])
    rs = []
    for ij in range(len(res)):
        rs.append(sum(res[ij]))
    rs = set(rs)
    if len(rs) == 1:
        print("#{} {}".format(i + 1, 1))
    else:
        print("#{} {}".format(i + 1, 0))

'''
1
7 3 6 4 8 9 2 5 1
8 5 2 7 3 1 6 9 4
9 1 4 5 6 2 7 3 8
4 9 7 2 5 6 8 1 3
5 6 3 1 8 7 9 4 2
2 8 1 9 4 3 5 6 7
6 7 5 3 2 4 1 8 9
1 4 9 6 7 8 3 2 5
3 2 8 1 9 5 4 7 6

'''
