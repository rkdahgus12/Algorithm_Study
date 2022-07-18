for i in range(int(input())):
    soo = int(input())
    res = []
    for j in range(soo):
        if soo == 1:
            s = input()
            print("#{} {}".format(i + 1, s))
            break
        res.append(list(str(input())))
    flag = True
    cot = 0
    if soo>1:
        for z in range(soo):
            if flag == True:
                cot += sum(map(int,res[z][soo // 2 - z:soo // 2 + z + 1]))
            if len(res[z][soo // 2 - z:soo // 2 + z + 1]) == soo:
                flag = False
                count = z
                break
        if flag == False:
            for z in range(soo // 2 - 1, -1, -1):
                cot += sum(map(int,res[count + 1][soo // 2 - z:soo // 2 + z + 1]))
                count += 1
        print("#{} {}".format(i + 1, cot))
