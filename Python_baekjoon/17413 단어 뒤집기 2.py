res = list(input().rstrip())
chk = []
st = ""
flag = False
for i in range(len(res)):
    if res[i] != "<" and res[i] != ">" and flag == False:
        if res[i] == " ":
            ls = list(st)
            ls.reverse()
            chk.append(''.join(ls))
            st = ""
        else:
            st += res[i]
    elif res[i] == "<":
        flag = True
    elif res[i] == "<" and flag == False:
        ls = list(st)
        ls.reverse()
        chk.append(''.join(ls))
        st = ""
    if flag == True:
        st += res[i]
    if res[i] == ">":
        flag = False
        ls = list(st)
        chk.append(''.join(ls))
        st = ""

if "<" or ">" not in st:
    ls = list(st)
    ls.reverse()
    chk.append(''.join(ls))
else:
    chk.append(''.join(ls))
print(*chk)
