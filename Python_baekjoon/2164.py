input = int(input())
res = 2
while True:
    if (input == 1 or input == 2):
        print(input)
        break
    res *= 2
    if (res >= input):
        print((input - (res // 2)) * 2)
        break
