def fibo(soo):
    if soo == 0:
        return 0
    elif soo == 1:
        return 1
    else:
        return fibo(soo - 1) + fibo(soo - 2)

print(fibo(int(input())))
