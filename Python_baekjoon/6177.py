import sys

input = sys.stdin.readline

soo = int(input())
res = []

for i in range(soo):
    a = int(input())
    res.append(a)
res.sort()
if len(res) % 2 == 0:
    count=(res[len(res)//2-1]+res[len(res)//2])/2
    print("{:.6f}\n{:.6f}".format(sum(res)/len(res),count))
else:
    count=(res[len(res)//2-1]+res[len(res)//2])/2
    if len(res)==1:
        print("{:.6f}\n{:.6f}".format(sum(res) / len(res), round(count)))
    else:
        print("{:.6f}\n{:.6f}".format(sum(res) / len(res), round(count) + 1))

# print("{}\n{}".format(sum((res)/len(res),)
