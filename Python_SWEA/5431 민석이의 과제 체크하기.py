for case in range(int(input())):
    a, b = map(int, input().split())
    res = set([i for i in range(1, a + 1)])

    ls = set(list(map(int, input().split())))
    st = ""
    for i in res - ls:
        st += str(i)+" "
    print(f"#{case + 1} {st}")
