import sys

input = sys.stdin.readline

soo = int(input())
num = sorted(list(map(int, sys.stdin.readline().split())))

# 짝수일 경우 가운데 값 중 작은 값을 출력
if (soo % 2) == 0:
    print(num[soo // 2 - 1])
# 홀수일 경우 가운데 값 출력
else:
    print(num[soo // 2])