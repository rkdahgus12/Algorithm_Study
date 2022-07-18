s = input()
s_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in range(len(s_list)):
    s = s.replace(s_list[i], "*")
print(len(s))
