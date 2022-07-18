for case in range(int(input())):
    n, m, k = map(int, input().split())
    res = list(map(int, input().split()))
    res.sort()
    num = []
    count = 0
    flag=True
    for i in range(n, m * n + 1):
        if i % n == 0:
            count += k
        for j in range(len(res)):
            if count < 0:
                break
            if res[j] >= i:
                count -= 1
                del res[0]
                break
            elif res[j]<i:
                flag=False
                break
    if count < 0 or flag == False:
        print("X")
        break

    if count >= 0:
        print("T")

'''
1
2 2 2
1 2
'''
