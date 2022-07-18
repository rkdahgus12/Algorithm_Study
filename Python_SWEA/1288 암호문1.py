for i in range(10):
    soo = int(input())
    res = list(map(str, input().split()))
    command_soo = int(input())
    com_res = list(map(str, input().split('I')))
    del com_res[0]

    for j in range(len(com_res)):
        slicing = com_res[j].split()
        for z in range(int(slicing[1])):
            res.insert(int(slicing[0]) + z, slicing[2 + z])

    print(f"#{i + 1}", end=" ")
    for res in res[:10]:
        print(res, end=" ")
    print()
