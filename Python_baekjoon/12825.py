# def knapsack(capacity, n):
#     if capacity == 0 or n == 0:
#         return 0
#     if size[n - 1] > capacity:
#         return knapsack(capacity, n - 1)
#     else:
#         return max(value[n - 1] + knapsack(capacity - size[n - 1], n - 1), knapsack(capacity, n - 1))
#
#
# a1, a2 = map(int, (input().split()))
# size = []
# value = []
# for i in range(a1):
#     s1, s2 = map(int, input().split())
#     size.append(s1)
#     value.append(s2)
# print(knapsack(a2, a1))  # 14
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])