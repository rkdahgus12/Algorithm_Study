soo = int(input().rstrip())

res = [0, 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for i in range(soo):
    x = input()
    if x == 'SUN':
        print("#{} {}".format(i + 1, 7))
    else:
        count = 0
        for j in range(res.index(x), len(res)):
            if res[j] == 'SUN':
                print("#{} {}".format(i + 1, count))
                break
            count += 1

