T = int(input())

for test_case in range(1, T + 1):
    count = 0
    flag = "0"
    num = input()

    for j in range(len(num)):
        if num[j] != flag:
            count += 1
            flag = num[j]

    print("#" + str(test_case) + " " + str(count))