soo = int(input())

for i in range(soo):
    a, b = map(int, input().split())
    sum = 0
    for j in range(a, b + 1):
        st = str(j)
        sum += st.count('0')
    print(sum)
