for i in range(10):
    soo, res = map(int, input().split())
    res = list(str(res))
    flag = False
    k = 1
    while k < len(res):
        if res[k - 1] == res[k]:
            del res[k - 1]
            del res[k - 1]
            k -= 1
        else:
            k += 1
    st = ""
    for z in res:
        st += z
    print("#{} {}".format(i + 1, int(st)))
