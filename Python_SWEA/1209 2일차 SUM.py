for i in range(10):
    soo = int(input())
    res = []
    ma = []
    for k in range(100):
        ls = list(map(int, input().split()))
        res.append(ls)
    for zz1 in res:
        ma.append(sum(zz1))
    for z1 in range(100):
        count = 0
        for z2 in range(100):
            count += res[z2][z1]
        ma.append(count)
    count = 0
    count1 = 0
    for x in range(100):
        count += res[x][x]
        count1 += res[x][100 - x - 1]
        ma.append(count)
    print("#{} {}".format(i + 1, max(ma)))
'''

'''
