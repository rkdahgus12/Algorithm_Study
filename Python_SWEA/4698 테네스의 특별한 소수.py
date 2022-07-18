# def isPrime(a):
#     if (a < 2):
#         return False
#     for i in range(2, a):
#         if (a % i == 0):
#             return False
#     return True
#
#
# for case in range(1, int(input()) + 1):
#     d, a, b = map(int, input().split())
#     count=0
#     for i in range(b + 1):
#         if (isPrime(i)):
#             if ("3" in str(i)) and a <= i <= b:
#                 count+=1
#     print(count)
n = 10 ** 6
a = [False, False] + [True] * (n - 1)
primes = []
count = 0
for case in range(1, int(input()) + 1):
    d, a1, b = map(int, input().split())
    for i in range(2, n + 1):

        if a[i]:
            primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
    # print("#{} {}".format(case, count))
    for j in range(len(primes)):
        if (str(d) in str(primes[j])) and a1 <= primes[j] <= b:
            count += 1
    print(count)
