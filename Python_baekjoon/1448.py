N = int(input())
x = []
for i in range(N):
    x.append(int(input()))
x.sort(reverse=True)
flag = False
for i in range(2, len(x)):
    if x[i - 2] < x[i - 1] + x[i]:
        print(x[i - 2] + x[i - 1] + x[i])
        flag = True
        break
if flag == False:
    print(-1)

'''
세 변의 길이를 알 때 (가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야)
두 변의 길이와 그 사이 끼인각의 크기를 알 때
한 변의 길이와 양쪽 끝각의 크기를 알 때
'''
