soo = int(input().rstrip())
for i in range(soo):
    a, b = map(int, input().split())
    res = []
    for k in range(a):
        ls = list(map(int, input().split()))
        res.append(ls)
    rsrs = []
    for i1 in range(a - b + 1):
        for i2 in range(a - b + 1):
            rr = []
            for j1 in range(b):
                for j2 in range(b):
                    rr.append(res[i1 + j1][i2 + j2])
            count = sum(rr)
            rsrs.append(count)
    print("#{} {}".format(i+1,max(rsrs)))
'''
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
