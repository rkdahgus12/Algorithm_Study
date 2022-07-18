soo = int(input().rstrip())
for i in range(soo):
    case = int(input())
    distance = 0
    speed = 0
    for k in range(case):
        command = list(map(int, input().split()))
        if command[0] == 1:
            speed += command[1]
            distance += speed
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0
            distance += speed
        elif command[0] == 0:
            distance += speed
    print("#{} {}".format(i + 1, distance))
