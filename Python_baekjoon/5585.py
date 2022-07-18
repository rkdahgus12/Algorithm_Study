money = 1000
soo = int(input())
money -= soo
count = 0
list = [500, 100, 50, 10, 5, 1]
for i in list:
    count += money // i
    check=money//i
    money -= check * i
    #print(money)
print(count)
