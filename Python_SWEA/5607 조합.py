for i in range(10):
    soo = int(input())
    a, b = map(int, input().split())
    combi = (a * (a - 1)) / (b * (b - 1))
    print("#{} {}".format(i + 1, round(combi % 1234567891)))
    