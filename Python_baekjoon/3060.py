# 현수가 1번부터 6번까지 돼지에게 각각 3, 2, 7, 1, 5, 4만큼 밥을 주었다면,
# 2번 돼지는 첫 날 받은 양 2에다 양쪽과 맞은편 돼지가 받은 양 15(3+7+5)만큼을 더해 17만큼 받기를 원한다.
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    result = 1
    total = sum(a)
    while total <= N:
        food = [0] * 6
        food[0] = a[0] + a[1] + a[5] + a[3]
        food[1] = a[1] + a[0] + a[2] + a[4]
        food[2] = a[2] + a[1] + a[3] + a[5]
        food[3] = a[3] + a[2] + a[4] + a[0]
        food[4] = a[4] + a[3] + a[5] + a[1]
        food[5] = a[5] + a[4] + a[0] + a[2]
        total = sum(food)
        a = food
        result += 1
    print(result)
