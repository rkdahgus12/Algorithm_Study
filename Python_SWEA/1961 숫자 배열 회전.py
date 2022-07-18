def case1(arr, z):
    st = ""
    for i in range(case):
        st += str(arr[case - 1 - i][z])
    return st


def case2(arr, z):
    st = ""
    for i in range(case - 1, -1, -1):
        st += str(arr[case - 1 - z][i])
    return st


def case3(arr, z):
    st = ""
    for i in range(case):
        st += str(arr[i][case - z - 1])
    return st


soo = int(input().rstrip())

for i in range(soo):
    case = int(input())
    ls = []
    for k in range(case):
        res = list(map(int, input().split()))
        ls.append(res)
    print(f"#{i + 1}")
    for z in range(case):

        print(case1(ls, z), case2(ls, z), case3(ls, z))
