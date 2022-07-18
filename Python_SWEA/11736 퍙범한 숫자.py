for case in range(1, int(input()) + 1):
    soo = int(input())
    res = list(map(int, input().split()))
    if soo == 3:

        if min(res) != res[1] and max(res) != res[1]:
            print("#{} {}".format(case, 1))
        else:
            print("#{} {}".format(case, 0))
    else:
        count = 0
        for i in range(1, soo - 1):
            if min(res[i - 1], res[i], res[i + 1]) != res[i] and max(res[i - 1], res[i], res[i + 1]) != res[i]:
                count += 1
            else:
                continue
        print("#{} {}".format(case, count))
