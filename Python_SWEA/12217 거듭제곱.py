for i in range(10):
    soo = int(input())
    a, b = map(int, (input().split()))
    sum = pow(a, b)
    print("#{} {}".format(i + 1, sum))
