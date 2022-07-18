for case in range(1, int(input()) + 1):
    soo = int(input())
    res = list(map(int, input().split()))
    ls=[]
    ind=[]
    for i in range(len(res)):
        ls.append(res.count(res[i]))

    print("#{} {}".format(case,res[ls.index(max(ls))]))
