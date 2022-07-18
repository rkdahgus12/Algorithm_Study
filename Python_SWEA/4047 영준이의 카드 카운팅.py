for i in range(int(input())):
    res = list((input()))
    ss = [res[:3]]
    ss_set = [''.join(res[:3])]
    for k in range(3, len(res), 3):
        ss.append(res[k:k + 3])
        ss_set.append(''.join(res[k:k + 3]))
    ss_len = len(ss_set)
    if ss_len != len(set(ss_set)):
        print("#{} ERROR".format(i + 1))
    else:
        ss.sort()
        s_count = 13
        d_count = 13
        h_count = 13
        c_count = 13
        for k in range(len(res)):
            if res[k][0] == 'D':
                d_count -= 1
            elif res[k][0] == 'H':
                h_count -= 1
            elif res[k][0] == 'S':
                s_count -= 1
            elif res[k][0] == 'C':
                c_count -= 1

        print("#{} {} {} {} {}".format(i + 1, s_count, d_count, h_count, c_count))
