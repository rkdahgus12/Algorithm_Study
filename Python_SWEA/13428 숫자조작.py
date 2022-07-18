soo = int(input().rstrip())
# 0이 아닌 작은수 min(y[y!=0]) # 방법 1
for i in range(soo):
    res = list(map(int, (input())))
    case = []

    for j in range(len(res)):

        for k in range(j, len(res)):
            temp = res
            temp[j], temp[k] = temp[k], temp[j]
            if temp[0] == 0:
                continue
            case.append(temp)
    # a, b = res.index(min(res)), res.index(max(res))
    # if a < b and 0 not in res:
    #     res[a], res[b] = res[b], res[a]
    #
    # print(res)

from itertools import combinations

for test_case in range(1, int(input()) + 1):
    N = input()
    cases = [int(N)]

    for a, b in combinations(range(len(N)), 2):
        temp = list(N)
        temp[a], temp[b] = temp[b], temp[a]

        if temp[0] == '0':
            continue

        cases.append(int(''.join(temp)))

    print(f'#{test_case}', min(cases), max(cases))
'''
4
12345
54321
142857
10000
'''
