from itertools import combinations

for case in range(int(input())):
    res = list(map(int, input().split()))
    ls = list(combinations(res, 3))

    num = []
    for i in range(len(ls)):
        num.append(sum(ls[i]))
    num = set(num)
    num = sorted(num)
    print("#{} {}".format(case + 1, num[-5]))
