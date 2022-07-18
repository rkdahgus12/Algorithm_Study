soo = int(input().rstrip())
for i in range(soo):
    s1 = int(input())
    res = list(map(int, input().split()))
    res.sort()
    print(f"#{i + 1}",end=" ")
    for k in res:
        print(k,end=" ")
    print()