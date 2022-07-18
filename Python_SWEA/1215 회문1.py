for i in range(10):
    soo = int(input())
    res = []
    for j in range(8):
        inp = list(input())
        res.append(inp)
    count = 0
    for k in range(8):
        for k1 in range(8-soo+1):
            chk1 = ''.join(res[k][k1:soo + k1])
            chk2 = res[k][k1:soo + k1]
            chk2.reverse()
            chk2 = ''.join(chk2)

            if chk1 == chk2:

                count += 1
    res1 = []
    for z in range(8):
        st = ""
        for z1 in range(8):
            st += res[z1][z]
        res1.append(list(st))

    for kk in range(8):
        for kk1 in range(8-soo+1):
            chkk1 = ''.join(res1[kk][kk1:soo + kk1])

            chkk2 = res1[kk][kk1:soo + kk1]
            chkk2.reverse()
            chkk2 = ''.join(chkk2)

            if chkk1 == chkk2:
                count += 1
    print("#{} {}".format(i + 1, count))
