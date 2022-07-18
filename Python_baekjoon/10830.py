import sys
import numpy as np

input = sys.stdin.readline

a, b = map(int, (input().split()))

arr = []

for i in range(a):
    arr.append(list(map(int, input().split())))
res = np.array(arr)
power = np.linalg.matrix_power(res, b)
power = power.tolist()

for i in range(a):
    for j in range(a):
        power[i][j] %= 1000
for i in range(a):
    print(' '.join(map(str, power[i])))
'''
import sys
import numpy as np

input = sys.stdin.readline

a, b = map(int, (input().split()))

arr = []

for i in range(a):
    arr.append(list(map(int, input().split())))
res = np.array(arr)
power = np.linalg.matrix_power(res, b)
for i in power:
    for j in i:
        print(j % 1000, end=' ')
    print()
'''
