T = int(input())

n = [int(input()) for _ in range(T)]

for q in range(T):
    s2 = n[q] ** 2
    s3 = n[q] ** 2 + n[q]
    if n[q] % 2 == 0:
        s1 = (n[q] + 1) * (n[q] // 2)
        print('#{} {} {} {}'.format(q + 1, s1, s2, s3))

    else:
        s1 = (n[q] + 1) * (n[q] // 2) + (n[q] + 1) // 2
        print('#{} {} {} {}'.format(q + 1, s1, s2, s3))