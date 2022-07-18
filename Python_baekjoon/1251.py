import sys
input = sys.stdin.readline

s = input().rstrip()
l = len(s)
answer = []
for i in range(l-2):
    for j in range(i+1, l-1):
        for k in range(j+1, l):
            new_s = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]
            answer.append(new_s)

answer.sort()
print(answer[0])