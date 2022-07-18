soo = int(input().rstrip())
for i in range(soo):
    s1 = int(input())
    res = []

    for j in range(s1):
        res.append(int(input()))
    count = sum(res) // s1
    su = 0
    for j in range(s1):
        if count - res[j] < 0:
            su += abs(count - res[j])
    print("#{} {}".format(i + 1, su))
