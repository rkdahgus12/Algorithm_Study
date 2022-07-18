for case in range(1, int(input()) + 1):
    res = input()
    x = sorted(res)
    x=''.join(x)
    if res == x:
        print("#{} Exist".format(case))
    else:
        print("#{} Not exist".format(case))
