import sys

input = sys.stdin.readline

a1, a2 = map(int, input().split())
re1 = set(list(map(int, input().split())))
re2 = set(list(map(int, input().split())))
ch1, ch2 = re1 - re2, re2 - re1
print(len(ch1) + len(ch2))
