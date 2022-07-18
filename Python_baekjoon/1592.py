person, cut, direct = map(int, (input().split()))
person_list = []  # 0부터시작 person-1까지
for i in range(person):
    person_list.append(0)
count = 0
cnt = 1
ball_touch = 0
cut_flag = False
while True:
    if person_list[count]==cut:
        break

    if person_list[count] == 0:  # 1->2 번째로 토스
        person_list[count] = person_list[count]+cnt
        ball_touch = ball_touch + 1
        if person_list[count] % 2 == 1:
            if count + direct >= person:
                count = (count + direct) % person
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
            elif count + direct < person:
                count = count + direct
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
        elif person_list[count] % 2 == 0:
            if count - direct < 0:
                count = person + (count - direct)
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
            elif 0 <= count - direct < person:
                count = count - direct
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
    elif person_list[count] != 0:  # 1->2 번째로 토스

        #person_list[count] = cnt
        if person_list[count] % 2 == 1:
            if count + direct >= person:
                count = (count + direct) % person
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
            elif count + direct < person:
                count = count + direct
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
        elif person_list[count] % 2 == 0:
            if count - direct < 0:
                count = person + (count - direct)
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
            elif 0 <= count - direct < person:
                count = count - direct
                person_list[count] = person_list[count] + cnt
                ball_touch = ball_touch + 1
print(ball_touch-1)
