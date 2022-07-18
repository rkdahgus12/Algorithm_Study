for case in range(1, int(input()) + 1):
    n, q = map(int, (input().split()))
    res = [0 for _ in range(n)]
    st = []
    for i in range(0, q):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            res[j] = i+1
    for j in range(len(res)):
        st.append(str(res[j]))

    print("#{} {}".format(case, ' '.join(st)))
