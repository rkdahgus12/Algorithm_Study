soo = int(input().rstrip())

for i in range(soo):
    res = set(input())
    s = []
    flag = True
    if len(res) == 2:
        print("#{} {}".format(i + 1, "Yes"))
    else:
        print("#{} {}".format(i + 1, "No"))
