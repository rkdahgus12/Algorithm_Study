for case in range(int(input())):
    l, u, x = map(int, input().split())
    if l <= x <= u:
        print("#{} {}".format(case + 1, 0))
    elif l > x:
        print("#{} {}".format(case + 1, l - x))
    elif u < x:
        print("#{} {}".format(case + 1, -1))
