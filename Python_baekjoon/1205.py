import sys

input = sys.stdin.readline

num, score, rank = map(int, input().split())
res = list(map(int, input().split()))

if num == 0 and score == 0:
    print("1")
else:
    if num == rank and res[-1] >= score:
        print("-1")
    else:
        rr = num + 1
        for i in range(num):
            if res[i] <= score:
                rr = i + 1
                break
        print(rr)
