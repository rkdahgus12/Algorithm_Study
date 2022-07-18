soo = int(input().rstrip())
for i in range(soo):
    res = list(map(int, input().split()))
    res.remove(min(res))
    res.remove(max(res))
    print("#{} {}".format(i+1,round(sum(res) / len(res)),1))
