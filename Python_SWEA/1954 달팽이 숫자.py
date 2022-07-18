for case in range(1, int(input()) + 1):
    soo = int(input())
    res = [[0] * soo for i in range(soo)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    nx = 0
    ny = 0
    ind = 0
    for i in range(1, soo * soo + 1):
        res[nx][ny] = i
        nx += dx[ind]
        ny += dy[ind]
        if nx < 0 or ny < 0 or nx >= soo or ny >= soo or res[nx][ny] != 0:
            nx -= dx[ind]
            ny -= dy[ind]
            ind = (ind + 1) % 4
            nx += dx[ind]
            ny += dy[ind]
    print("#{}".format(case))
    for j in res:
        print(*j)