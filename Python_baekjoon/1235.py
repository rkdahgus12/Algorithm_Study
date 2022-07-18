import sys

# a=['12345']
# print(a[0][3:])
ip = sys.stdin.readline
soo = int(ip())
res = [ip().rstrip() for _ in range(soo)]
str = res[0][-2:]
count = 0
for i in range(len(res[0]) - 3, 0, -1):

    if count == soo - 1:
        print(len(str))
        break
    count = 0
    str = res[0][i] + str
    for j in range(1, len(res)):
        if res[j][i:] != str:
            count += 1
            continue
'''
4
123456
125426
126456
127226
'''
