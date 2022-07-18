for case in range(1, int(input()) + 1):
    d = 11
    h = 11
    m = 11
    res = list(map(int, input().split()))
    d = (res[0] - d)*24*60
    h=(res[1]-h)*60
    m=res[2]-m
    print(d+h+m)


116,511
(11*24*60)+(11*60)+11
15840+660+11