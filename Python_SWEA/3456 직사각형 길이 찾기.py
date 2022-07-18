for i in range(int(input())):
    res = list(map(int, input().split()))
    res.sort()
    com = res[0]
    for k in range(len(res)):
        if res.count(res[k]) == 1:
            num = res[k]
            print("#{} {}".format(i + 1, res[k]))
            break
        elif res.count(res[k]) == 3:
            print("#{} {}".format(i + 1, res[0]))
            break
