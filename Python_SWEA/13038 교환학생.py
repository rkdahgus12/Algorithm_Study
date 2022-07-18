
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    li = list(map(int, input().split()))
    answer = []

    for i in range(len(li)):
        if li[i] == 1:
            T = n
            sum = 0
            while T > 0:
                if li[i%7] == 1:
                    T -= 1
                i += 1
                sum += 1
            answer.append(sum)
    print("#{} {}".format(test_case, min(answer)))
