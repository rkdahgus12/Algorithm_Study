for case in range(int(input())):
    a, b = map(int, input().split())
    if b >= 10 or a >= 10:
        print("#{} {}".format(case+1,-1))
    else:
        print("#{} {}".format(case+1,a * b))
