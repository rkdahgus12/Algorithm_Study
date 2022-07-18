N = int(input())
score = list(map(int, input().split()))
score.sort()
sum = score[N - 1]
for i in range(N - 1):
    sum = sum + score[i]
print(round((sum/score[N-1]*100)/N,6))
