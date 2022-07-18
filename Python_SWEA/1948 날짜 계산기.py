soo = int(input().rstrip())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(soo):
    res = list(map(int, input().split()))
    if res[0] == res[2]:
        print("#{} {}".format(i + 1, abs(res[1] - res[3]) + 1))
    else:
        count = sum(month[res[0] - 1:res[2] - 1]) - res[1] + 1 + res[3]
        print("#{} {}".format(i + 1, count))
