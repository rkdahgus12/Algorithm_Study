# import math
#
#
# def is_prime_num(n):
#     for i in range(2, int(math.sqrt(n)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
#         if n % i == 0:
#             return False
#
#     return True
#
#
# for i in range(2, 1000000):
#     if is_prime_num(i) == True:
#         print(i, end=' ')
  ##에라토스테네스의 체
N = 10 ** 6 + 1
eratos = [1] * N
eratos[0], eratos[1] = 0, 0

for i in range(2, N):
    if eratos[i] == 1:
        for j in range(i * 2, N, i):
            eratos[j] = 0

for i in range(N):
    if eratos[i] == 1:
        print(i, end=' ')
