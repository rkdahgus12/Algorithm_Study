def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


a_list = list(range(2, 10000))
memo = []
for i in a_list:
    if isPrime(i):
        memo.append(i)
x, y = 0, 0
min2 = 999999999
soo = int(input())
a = []
for i in range(soo):
    inp = int(input())
    for ii in memo:
        if ii > inp:
            break
        for jj in memo:
            if jj > inp:
                break
            if ii + jj == inp and min2 > abs(ii - jj):
                x, y = ii, jj
                min2 = abs(ii - jj)
    if x > y:
        print(y, x, end=" ")
    else:
        print(x, y, end=" ")
    x, y = 0, 0
    min2 = 999999999
    a = []
