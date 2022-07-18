import sys

input = sys.stdin.readline
n = input().split()
n[0] = n[0].replace('XXXX', 'AAAA')
n[0] = n[0].replace('XX', 'BB')
if 'X' in n[0]:
    print(-1)
else:
    print(n[0])
