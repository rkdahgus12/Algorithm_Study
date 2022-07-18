from itertools import permutations

for i in range(int(input())):
    N, M = map(int, (input().split()))
    res = list(map(int, input().split()))
    ss = list(permutations(res, 2))
    rr = []
    for j in range(len(ss)):
        rr.append(sum(ss[j]))
    rr = list(set(rr))
    rr.sort(reverse=True)

    flag = True
    for k in range(len(rr)):
        if M >= rr[k]:
            print("#{} {}".format(i + 1, rr[k]))
            flag = True
            break
        else:
            flag = False
    if flag == False:
        print("#{} {}".format(i + 1, -1))
