soo = int(input().rstrip())

for i in range(soo):
    a = int(input())
    count = 0
    for j in range(1, a + 1):
        if j % 2 == 1:
            count += j
        else:
            count -= j
    print("#{} {}".format(i + 1, count))
