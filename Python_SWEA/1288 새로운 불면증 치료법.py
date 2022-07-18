chk = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for case in range(1, int(input()) + 1):
    soo = int(input())
    a = set(str(soo))
    for i in range(2, 10 ** 6):
        k = set(list(str(i * soo)))
        a = a | k

        if chk == sorted(a):
            print("#{} {}".format(case, i * soo))
            break
