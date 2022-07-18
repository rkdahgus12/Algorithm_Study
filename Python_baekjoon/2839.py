N = int(input())

cnt = 0

while True:
    if N < 0:
        print("-1")
        break
    if N % 5 != 0:
        N = N - 3
        cnt = cnt + 1
    elif N % 5 == 0:
        cnt = cnt + N // 5
        print(cnt)
        break
