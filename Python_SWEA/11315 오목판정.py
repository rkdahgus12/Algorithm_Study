def A(arr):
    # 우,하,우하대,좌하대
    dr = [0,1,1,1]
    dc = [1,0,1,-1]
    for start_r in range(N):
        for start_c in range(N):
            if arr[start_r][start_c] == 'o':
                for d in range(4):
                    r = start_r
                    c = start_c
                    # 각 방향으로 연속적으로 오목이 존재하는가?
                    cnt = 0
                    # 파이썬만 0 <= r <= N-1 허용
                    # 다른 언어는 r >= 0 and r <= N-1
                    while 0 <= r <= N-1 and 0 <= c <= N-1 and arr[r][c] == 'o':
                        cnt += 1
                        r += dr[d]
                        c += dc[d]
                    # 각 방향으로 오목이 존재?하는가
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

# 테스트 케이스의 개수
T = int(input())
for tc in range(1,T+1):
    # N*N 크기의 판
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc} {A(arr)}')


def check(res):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for i1 in range(soo):
        for j in range(soo):
            if res[i1][j] == 'o':
                for k in range(4):
                    r = i1
                    c = j
                    cnt = 0
                    while 0 <= r <= soo - 1 and 0 <= c <= soo - 1 and res[r][c] == 'o':
                        cnt += 1
                        r += dr[k]
                        c += dc[k]
                    if cnt >= 5:
                        return "Yes"

    return 'NO'


for case in range(int(input())):
    soo = int(input())
    arr = [input() for _ in range(soo)]

    print("#{} {}".format(case + 1, check(arr)))
