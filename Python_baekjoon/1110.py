soo = int(input())
result = soo
count = 0
while True:
    one = result // 10
    two = result % 10
    result = two * 10 + ((one + two) % 10)
    count = count + 1
    if result == soo:
        print(count)
        break
