soo = int(input().rstrip())

res = []
for i in range(soo):
    res.append(list(map(int, input().split())))
for j in range(soo):
    a, b = (res[j][0] / res[j][1]), (res[j][2] / res[j][3])
    if a == b:
        print("#{} DRAW".format(j + 1))
    elif a > b:
        print("#{} ALICE".format(j + 1))
    else:
        print("#{} BOB".format(j + 1))
