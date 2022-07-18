import sys

input = sys.stdin.readline
count = 0
index = 0
while True:
    index += 1
    L, P, V = map(int, input().split())
    if L + P + V == 0:
        break
    else:
        count = (V // P) * L
        count += min((V % P), L)
        print("Case %d: %d" % (index, count))
