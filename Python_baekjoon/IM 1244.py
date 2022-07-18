soo = int(input().rstrip())

res = input().split()
per = int(input().rstrip())

for i in range(per):
    a, b = map(int, (input().split()))
    if a == 1:
        for j in range(b, soo, 3):

            if res[j - 1] == '0':
                res[j - 1] = '1'
            else:
                res[j - 1] = '0'
    else:
        count=0
        for k in range(b, 0, -1):
            count+=1
            if (res[k - 1] == res[b + abs(k)]) and res[k - 1] == '1':
                res[k - 1], res[b + abs(k)] = '0', '0'
            elif (res[k - 1] == res[b + abs(k)]) and res[k - 1] == '0':
                res[k - 1], res[b + abs(k)] = '1', '1'
            else:
                if res[b] == '0':
                    res[b] = '1'
                else:
                    res[b] = '0'
                break
