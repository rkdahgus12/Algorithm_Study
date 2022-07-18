soo = [input()]
soo_1 = 0
soo_2 = 0
flag_1 = True
flag_2 = True
for i in range(len(soo[0])):
    if soo[0][i] == '0':
        if flag_1 == True:
            soo_1 += 1
        flag_1 = False
        flag_2 = True
    elif soo[0][i] == '1':
        if flag_2 == True:
            soo_2 += 1
        flag_2 = False
        flag_1 = True
print(min(soo_1, soo_2))
