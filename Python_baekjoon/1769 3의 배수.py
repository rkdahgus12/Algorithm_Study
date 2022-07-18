soo = list(map(int, input()))
count = 0

while True:
    if len(soo)==1:
        if sum(soo)%3==0:
            print(count)
            print("YES")
            break
        else:
            print(count)
            print("NO")
            break
    su = sum(soo)
    count += 1
    x = su
    su = list(map(int, str(su)))
    if len(su) == 1:
        if x % 3 == 0:
            print(count)
            print("YES")


            break
        else:

            print(count)
            print("NO")

            break
    soo = su
