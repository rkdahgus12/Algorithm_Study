for case in range(1, int(input()) + 1):
    st = ""
    soo = int(input())
    for i in range(soo):
        a, b = map(str, input().split())
        st += a * int(b)
    print("#{}".format(case))
    for j in range(0, len(st), 10):
        print(st[j:j + 10])
