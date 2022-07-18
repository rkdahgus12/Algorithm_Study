for i in range(10):
    soo = int(input())
    res = []
    for k in range(soo):
        ls = list(map(int, input().split()))
        res.append(ls)
    count = 0
    for z1 in range(soo):
        flag = True  # true 면 N
        for z2 in range(soo):
            if res[z2][z1] == 1 and flag == True:
                flag = False
            elif res[z2][z1] == 2 and flag == False:
                flag = True
                count += 1

    print("#{} {}".format(i + 1, count))

'''
2 0 1 0 2 0 2
0 1 0 0 0 0 0
0 0 2 0 0 2 0
0 0 0 0 2 1 1
0 0 0 0 0 2 0
0 0 1 2 0 1 2
0 0 2 1 1 0 1
'''
