soo = int(input())
for i in range(soo):
    st1 = input()
    st2 = input()
    if st1 in st2:
        print("#{} {}".format(i+1,"N"))
    else:
        print("#{} {}".format(i+1,"Y"))