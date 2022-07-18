def chk(res, s, k):
    for i in range(s[0], max(mas) + 1):
        for j in range(s[1], max(mas) + 1):
            if res[i][j] == "#":
                k -= 1
    if k == 0:
        return True


for case in range(1, int(input()) + 1):
    soo = int(input())
    res = []
    mas = []
    for i in range(soo):
        res.append(list(input()))
    for i in range(soo):
        ma = 0
        for j in range(soo):
            if res[i][j] == '#':
                ma += 1
                mas.append(ma)
            else:
                ma = 0
    k = max(mas) ** 2
    chk1 = max(mas)

    if k == 1:
        print("#{} no".format(case))
    else:
        s = []
        flag = True
        for i in range(max(mas) + 1):
            for j in range(max(mas) + 1):
                if chk1 == 0:
                    if chk(res, s, k) == True:
                        flag = False

                    s.append(i)
                    s.append(j)
                if flag == False:
                    break
                if res[i][j] == "#":
                    s.append(i)
                    s.append(j)
                    chk1 -= 1
                else:
                    chk1 = max(mas)
        if flag == False:
            print("#{} yes".format(case))


        else:
            print("#{} no".format(case))
'''
1
6
#.#.##
......
###...
###...
###.##
.#.###
'''