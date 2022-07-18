for i in range(10):
    soo = int(input())
    res = list(map(int, input().split()))
    for s in range(soo):
        x = max(res)
        y = min(res)

        res[res.index(max(res))] -= 1
        res[res.index(min(res))] += 1
    print("#{} {}".format(i + 1, max(res) - min(res)))

'''
11
5 8 3 1 5 6 9 9 2 2 4
'''
