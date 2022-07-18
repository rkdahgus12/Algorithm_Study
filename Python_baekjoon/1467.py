# import sys
#
# input = sys.stdin.readline
# soo = list(input())
# soo1 = list(input())
# flag = True
#
#
# def unique(soo1, flag):
#     if len(soo1) == len(set(soo1)):
#         flag = True
#         return flag
#     else:
#         flag = False
#         return flag
#
#
# if len(soo1) == 2 or unique(soo1, flag) == True:
#     common = []
#     for i in soo1:
#         if i in soo:
#             soo.remove(i)
#             common.append(i)
#     print(''.join(soo))
# elif unique(soo1, flag) == False:
#     common = []
#     for i in soo1:
#         if i in soo:
#             soo.remove(i)
#             common.append(i)
#     soo = sorted(soo, reverse=True)
#     print(''.join(soo))

import sys
from collections import Counter
input=sys.stdin.readline
seq = input()
R = input()
cnt = Counter(seq) - Counter(R)
ans = ''
idx = 0
while cnt:
    for i in range(9, -1, -1):
        num = str(i)
        if cnt[num] < 1:
            continue
        t = seq.find(num, idx)  # 이 수가 들어갈 자리 확인
        # 마지막으로 채워넣은 수 다음 자리부터 찾아야 해서 idx를 넣음
        check = cnt - Counter(seq[t:])  # 남은 애들을 뒤에 있는 숫자들에 채워넣을 수 있는지 확인
        if check:  # 여기에 숫자를 배치하면 뒤에 애들로 남은 숫자들을 배치할 수 없는 경우
            continue
        else:
            ans += num
            idx = t + 1
            cnt[num] -= 1
            if cnt[num] == 0:
                del cnt[num]
            break  # 다시 제일 큰 수부터 찾아야 올바르게 찾을 수 있다.

print(ans)
