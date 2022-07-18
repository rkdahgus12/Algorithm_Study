# for i in range(1):
#     soo = int(input())
#     res = list(map(int, input().split()))
#     out = []
#     for j in range(0, len(res)):  # 4일때
#         x, y = 0, 0
#         if res[j] == 0:
#             continue
#         elif res[j] != 0:
#             if j >= 2:
#                 if res[j - 2] != 0:
#                     if res[j - 2] > res[j - 1] and res[j - 2] < res[j]:
#                         x = res[j] - res[j - 2]
#                 if res[j + 2] != 0:
#                     if res[j + 2] > res[j + 1] and res[j + 2] < res[j]:
#                         y = res[j] - res[j + 2]
#                 out.append(max(x, y))
#     print(sum(out))

'''
14
0 0 3 5 2 4 9 0 6 4 0 6 0 0
'''
for t in range(1, 11) :
    N = int(input())
    build = list(map(int, input().split()))

    view = 0
    for i in range(2, N-2) :
        a2 = build[i] - build[i-2]
        a1 = build[i] - build[i-1]
        b1 = build[i] - build[i+1]
        b2 = build[i] - build[i+2]
        if a2 > 0 and a1 > 0 and b1 > 0 and b2 > 0 :
            view += min(a2, a1, b1, b2)

    print("#{} {}".format(t, view))