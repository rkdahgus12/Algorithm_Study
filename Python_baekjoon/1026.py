soo = int(input())
res_1 = list(map(int, input().split()))
res_2 = list(map(int, input().split()))
res_1.sort()
res_2.sort(reverse=True)
count=0
for i in range(soo):
    count+=res_1[i]*res_2[i]
print(count)