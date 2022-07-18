for i in range(int(input())):
    chk = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    a, b = map(str, (input().split()))
    res = list(map(str, input().split()))
    res_res = []
    for k in chk:
        res_res.append(res.count(k))
    st=""
    for z in range(len(chk)):
        st+=  (chk[z] + " ") * res_res[z]

    print("#{} {}".format(i + 1, st))
        # print("#{} {}".format(i + 1, chk[z] * res_res[z]))
