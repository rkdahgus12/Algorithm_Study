for i in range(10):
    x = int(input())
    soo = 99
    res = []
    for j in range(100):
        inp = list(input())
        res.append(inp)
    count = 0
    while True:
        if count > 0:
            break

        for k in range(100):
            for k1 in range(100 - soo + 1):
                chk1 = ''.join(res[k][k1:soo + k1])
                chk2 = res[k][k1:soo + k1]
                chk2.reverse()
                chk2 = ''.join(chk2)

                if chk1 == chk2:
                    count += 1
        res1 = []
        for z in range(100):
            st = ""
            for z1 in range(100):
                st += res[z1][z]
            res1.append(list(st))

        for kk in range(100):
            for kk1 in range(100 - soo + 1):
                chkk1 = ''.join(res1[kk][kk1:soo + kk1])

                chkk2 = res1[kk][kk1:soo + kk1]
                chkk2.reverse()
                chkk2 = ''.join(chkk2)

                if chkk1 == chkk2:
                    count += 1
        soo -= 1
    print("#{} {}".format(i + 1, max(len(chk1), len(chkk1))))
'''
1
CCBBCBAABCCCBABCBCAAAACABBACCCCACAABCBBACACAACABCBCCBAABCABBBCCAABBCBBCACABCAAACACABACBCCBAACBCBCAAC
ACBAAAACCACCCBAACAAABACACCABCBCBABBBACBABCAACCBCCACBCBACACACBCACCABACCBCCBAAAAABBACBACACBCCBABCAACBB
CCCACCBCBACBACBCABAABABCCAAAACCCCCBBAABBCCBCCCABBACACAACBCCCBAAACACABCCABCCCCCABCAAAABBBCBBBAABCCACC
CABACBCBBCBABACABBBBBBABBCABCBCBCAABCBCCCBABACCCCABBABBBACBBACBCCCAAACACCABABCCCBCACCBCBCAACACBCCBAC
BCCBCCACCBCBCABBBCCABAACACCBCCCBCCACCBBCBCCCBBCCBACBCBCBBCBABCBACBBABABCBCACBAAABBABACABBCBCCBACCBBC
BBBBCBBAACABACCBCBCCABBBBCCAABCBBCACCBBCAAAABABABBABBBACAAABAABACCBCAACCAABCBBACCACBABBCCCACCBCABCAC
ABBAACCCACBBABBABCCCABABCACABABACCCBACACABCBCCCBABCCCCABCBAABBAAABACCCCABBABABAACABBCACBACACBBCBAABA
ABBBBAABCAACCBACBBAACACABCABACBAABCAABBCCCCCCACBCCCCAABCBABAABCBBAAACCCCCABAAAABCAABBCCCCACCBACABABB
ACCACABABBACBBAACCBBACBBCCACCACCABCCBABABBBACBACBAABCBBCAACAABABBABBAACABCAABCCABACBBBBCABCCCACBACBA
BABACACCABCAACBAABCCACCACBCCAABBCBAABABAACAAAAAACCCBCBBABBBBBCBCACBABABACBBABCBABBCACBCACCBCAAABACAA
ABABACAABABCACCBABABCABCABABBAABABCBABBCABBACCCBBBCCACBACCCBCCAABCAABCBBBCCBACCBABCAACACAABABABACABB
CBBACCACBBBCBABCCACCABCACABAACBBACBACCAABCAAAAACCCABBAABAABCBACCCBCBABACCBCBAABAAACABBAABABBBBBCABAA
AAAABACBBAABBAABBCACABBCBBCAABBCBAAAAACBABCAACAAACAACBCCCBCBABABBCBCACBCAACCAABBBBBACABAAAABCAABABBC
CBCCBCCBBABABBBAACBACCCAACBCBCCABCCCAAABAACBBCACACAAABCCCCBCBBAACACAACCBAACBABAACCCBBBCCCAACBCACBCBB
BBCBCCACCCCABCBCACCBBAACAABAABCCAACCCABABCCBCABBBAAABABBBBAABBCACBBAACCBCAACACACAAACBCACBAACACCABCCA
AAACBAABBCCBAAACCBBBCABABBAACBABACBCBAACABCBABABAABCBCBABAABCACACABAACBBBABCABAACBBCBCCAACCCCACAABAA
ACCBACACCCBABCBBBBBAACABBBBBBBACACCABAACBCBAACBCBCBBCCCBAAABACCBBACBCCBAABACBACCBBBBCCCCCACCBCCAAAAB
ABAACCCCCCBBBBBBABACAABBBCCBCBAAACCBCABBCCABBABBABCBCBCCBBABABCBBBAACBBAACCCCBCCABBABAAAABCCBAAABCBB
AACBACAAAABCABBABABCBBABCABAAACBABCABAAABBBCCAACCAABBCACCCCABCACCCBCBCBBBBBBBACBAACCCCCABACABBCCBBCC
BCBCABABABCBABBCAACCCCBBCACACCCCACBACAABCCCCABCACAAACCABCACCBCCCBBAABBBCBCCCCCBBBCABCBAABABBAACAACAB
AAABCAAABABABCBBCACCAABABACCCABABABABAAAAACAAAABCBAAACABACCBCBBAAAABBBAAACBABABABCABAACAABCCBCCBBCCC
ABCACCBACBCAACACCAAACCCBABBAABCABBBBCACABACCCBCABCACACBCBABBBBAAAAAABCCCCACBCBCBBBABBABBCABCCABACAAB
BCCCBBABAACCCAABCABAABACACBCACBABBBCCBACAAACAAAABCABBBABACCACCBACBACBBBCBCACCCABBABCACCABCCACBCBAAAA
CCBACACCBCBCACBCACCBCACBABACBCBACBACAAAABABBBAAABBBACACABBBCBCAACBCCCBBABABABCABAAABCCCBBBBAAABBCCCC
BBAAACCACACACBABCBABBABCAACACAACCCCBCCABBBACCACCCAABBABABCABCCCAACBABBCBABCABBCBAACACBCBCCABAAAAAAAB
CBABBCCCACACBBABCBABBABCBBACABBAACACBBCBBBBABABAACBBBCCACBBBAACCABCBACBABBABCACACCBAACBAABAABCABBBAC
BBBCCABAABCABCBBCCBBACBBCBAACBBCCCCABACBABBCABBBBCCBBCCBCBACACBABCACCAABABCCBBACABBBCCAABBAACABCBCBA
CABACAAAABCBBBABCCACBCACBCACCBAACCCCBBAACBBBBAACACABBBCBACABCABABABCCACABAABCBBABABBCBABABABCCBCCCBA
ABABBCBACCCCAAABCABAAABCCABBBBACAAACCAABCACAABBCCBAACAACCBCCACCCBABCBAABCAABABBACACBCBBCCCACBBBBCCBA
CCAABCCABABACBCACBACCBBACCABBABAAAABAABBCBACCCBCBAAABCCAACBBCCAABABCCACAAACBBCCCBCAAACCCBACCACBAACAC
AAABBCABABAACBAAACBBBAABCACBCABCBBCBBCBCCBACBABBBABAAABBACCACBABACBACCACBACCBCCCBCBBAACBCACBACCBACAC
ABCAABCABCABBCAAAACABABBABBBCCCCCBBABCCCAABAAACACCCBABACABCBBCCAABCACBAAAABBACCACACACBAABAABABCAAACC
AAACBCAABBACCCAAAAAABCBAAAACCBBCBCBCCBCBCCBBCCBABBAACACCABBCCACACABABABCCBBCBAAACCCCABABACCABBBCCBAA
BAABCBABAAAACBABBCABACCCACAACCCCACBABBBBABBCACCBBCACBBCBCAABBABBBACBCBCBCBAACCBBAABCBAABBABABABBABBC
BABACBBCACBBABABCABCCCBCAACAAABACAACABBBABBBCBABAABABBBAACAACCCBACCCBCCABBCAACCCABBCBBCCBCBBBCABACCC
ABCABABBAAAACBACCCBABBBABACCBACBCAABAACCCBACAAABCBAACCCBBBACAABBAAAAACCCACACCABCCACABCCCAAABCCCACABB
BACCBBACABCABAACBCABBCBBBBBACBBACCABBCAACAABAABBBCCABAAABBABBCAAABCBACCBABCCBBABCABBBCACBABBCCCACCBC
BBBCBBCCABACCBCACBBAAACABCABAABBBBCAACBBCCCBBBBBCAABACAACBCCABAAACCABCBCCBBAAABAABBBACBACAABBABACBCB
BAAABACCBBAACACBCCABBBCBBBBCCCBBCCBABBABBABBACAAABCCBBBCCCCBAAACCBCCCAABACBBAACCABACBCBABBBBBCCBBACA
BCCACAACAABBBAABCBAABABABAACCCACCBCCBABABBAAACCACCCBCABCBAAACBCBCCBBCCCBBBACCABBACBBBCBABACCCCABACCB
BBBCAAACBACCAAABACBCAACBACBCCBACBBCBBABBBABACABCABCABACCBABCBABBABACBBCBABAAAABACBABAABCBCCBAAACBBAC
BABACBBBBACCCCBBCBACACCAAABCBBABACBAAAACBCBBAAAABABBBABCCCACCBBBCBCBCABBCBBABACCBACCCCACBABBBBCCBBAB
CBBCABAAACACBABABBAACBCACACBABBABCABCBCBCCACAAACABCBCABACBCBACCACAAABAABBACAAAACCCBBCBCABCCBACCBCCAB
CBCCCBAAABABBACBABCACACBBBBBACACBABACBCCACBBCBCACABABAACAAACBBACAAAABCCCCACBCCBBCBBCCCACBBABCCBCBBBA
ACACCBCABBBBABCACABCABABCCBBCAACBAAABAABBBACBCBCCBCAAAABCCCABAACABBACCABABBBBCBCAAAAABAACACBCBCAAAAB
ACBBBBCCABABABBAACCACCCACABBBABCAACBBBAABACCABCCBBBCBBCCABABABCBBCCABBBCCCACBCCCACCCBBAACABACBCABBAC
CCCCBBCCACCCCACBABBAABAACCACCCCBCCCAACCCCBACAAABBAAABACAAACABACABABCAAACBABCBCBACCBBBBBBBCCACABCBCBB
CBBBBCBACABCACCBBCAACAACCABBBCCACCCCCBBCBBACABCBCACCBABACBCBCACABCCACCACBCBCBAABCABABACBABABBABBBCAA
ABAACAACBCCBAABBBBBCBCBCCAABAACBABBABBBABCABBAABAAAACBBBAABAAACBABBBCAABCCBCBABBACBAABAACBAABABCBACA
BCAACACBBCBBACBBACCACBBCABBCCBCBACBBBABBCAAACABCCBCBCCABCACACBACACCCBAACBBACBBAACBACCCACBBABABCAABAB
BBBBAABBAABCACCBBBBBAAACCBCAABCACAACACBBBCBBCAABBBBACCACACACABCACABCACBBCCCBAACACABCBBABABABACABABBB
CBCCCBACCBABBACCABBBCBAACCBBCBABCBCABCABBAAACAACAACBCCACBCCACBACABCBBBABACCABBCCCAAABABBABCBBCCAAACB
AABABCBCBABBBCAABBBABABCBBBACBCBACBCBAACABCCBAACABCABCCCABABCABBAAACCBAACCBACACACABBCACCAACABBABACAC
CBACCACCCCCBBACCCACABCBBCACCBCCCBCBBACCBBACACCCCACBABCCACACBBBBBBABBBBCCABAAAACBBCCBBAAAABCBBCACBAAC
ABAAABBABBCCABBACCABBABCCACCAACCCACBCCBBBABCCBCCBACBBBAAABCBBBBBAAACACAABCBCCBACCBBBCBCAAABCBBCCCCBC
CBCCCBCACCBAABCABBCACCABACAACACBCCBAABBACAAAACCBCBABACCCAAACACCBABBBBBCCACCACAABCACAAAAAAAAACBBCBACA
CBBCBCCABCBCCBCCACABCACBACABCBCCBBCBABCBBCCABCCCACCBBCCCACACCCBABAABBCCCCCCBBAABBCBCACBABAAACAACBCCC
CACAACAABBCABACAAABCCBBBACBCABCBCBBCAAACAABBAAABBBCBAAACCAAAACBAAAABAACBAABACCAAAABCCCBBCAABBBAACCBA
BACBBBCCACBBACABABBBABCCACCAABACCCCCAABBABCBACCBBBCCBABBCBCCBCACBBBBAAABACCCBBAABBCBCACCBAABABBABBCB
BCBACBCBBCBAABAABCCABBAAAACCBBCCACCACCCCCACBCCBBCCAACACBBAABBCCACABCCBABBBCAAABACCCBBABBCBACBABCAABB
AACACAACABAACCBBCCBCCCBBACACCAACCABCAABAAACCACABBAACBCCBBABBACABCCAABACAAABAABABCAAABBCAABAACCACABBA
BABAACABABCCABCACBBCCCBCAAAAACCCCABAAABBBBBBAACABCCCCBCBCCABBCACCAAACAACCAACBACCACBCACBBBBBBACBAABCC
BCCBCAACAAAACABAACBBCCCBAACACAAABACCAACBAABCBBBBACAACBCCABCCABBBACBCABCBACCACBCCBACABCACBCCABCCAAACB
CCBCAABBACBCBBBCAAAACACBBBBACAACAAABBCCABCCCABBBCABAABCBACCACAABCBBACBCAABACBAABABCABACACCBAABABCBBB
CCABCCABBBABABBBCCCABABBAAACCCBBCAACACCBAAACBBBAACABACABBCACCBCBACBBABABCAACAACCAAABCCCCACABAABACCBC
CAACABBCBACACCCBACBABBAAAAABBAAABBAACCBCBACACCACBBBBBCABAABBCCCABCCBBCABBCBBBCCCABCBCACACABBBCCCACAA
BACCBAACACBCBCAAAAABABABBACACABACCBBCCBABACBABBCACACBBACBCAABAACCBBAABBCBBBBBBCBABABAACBBBBBAABAABCA
ACBCBCCCBCACACACBCABABCCCBCCAACACCABAAACABBAACCABBBCCAAABACBABBAABAABCCCAACBABCBAAAABABAAABACCCCBCAC
AAAAAACABBAABAACBCCCBCCACBABCBABCCBABCBCAABBCABBABBAACBBBAABBBCBBCBBCBCBBBCACABCCCABBBBAABCCACCCACAB
AAACBBBACABAABBCCACCCAACCCCABACCCBCACBBBBABACACCBABBABBAAABCCBCACACBCABBCABAACBACBCCCAAABCBCCBBBAAAC
CCBACACABBBBBACBBBCACCAABAACBCACAAABCCCBCBBBABAAABCABAACBCCACCCCACCCBAABBCCBBBBCACCBCCCBBACBCABBBAAB
CABCBACCABCCCBBBAACCCBCBBBCBCCBABAABCACCABAAAACCCACBCBBBABAABCBBBAABCCBCACBBBBCBBCABBBBBABBCCACABBAA
CABAACCAABACBABACACBCAABBCACCAABAACBBCAABBBAAAAACABBBBACBCCCCCAABCBABCCBABCBCCABACAACBCCABBBCABABACA
ACCBACBCABCACACCBCABBCAABABCCCCCACCABBCCACBBABCACCBBCABCABBABBACCCBBBCCBBABACCCAABACBCACCBACBCCCBABA
BCCCCACACBBCCABBBCCAABCCBACCABAABBBCBCCCACAACCABBCCBABABACBCAAABBABAABAAACABBACBBBACBCCBCAABACACCCCB
BBAACABBCCBCABBCACCBCCCAAACCAAACBCAABCBBACABABBCBCABBACACAABABACCCCBABABCCBAABBABBCCBBCCABBCABCACCBA
AACAABCCCCCBBAACABCAACACCBACAACBBBBABACAACCACBCBBCAACBBACACBACBACAACACACABCAAAACACBCBACCABCBACABCCCC
CBACAABABBBCCABAACBAACBBBCACABBCAACAAACABCBCBCBCCBBCCACCCCBAACCBCACCABAAABABAABBABCABBBBABCABBCCCACA
AAAABCCBACACABCCBCCABACACACAAACBCCCCABAACAAACCACABBAABACBBAABABBCCCCBABBAACABCABBACBCCBABAAACABAAABB
BBABACCCBCACAABCBAAACBBBBBCABABCBAABABBBABCBACACBBCCBBCABBBAACCCACCABBABBCACCBBAAACBAABABBABBAAABBBB
BBCACBACCAAAAACBCBAACABAACABAACACCACABABBACBBAABCACABCCBBABBACBAAACBBCAACCAAABACCCBBACCBABABAACAABAC
CCBCBBCCBABBABCBAABCAACCAAACCCABCBBCBBABABBAAABBBCAACBABBBBBBACACCBBCBAACCAABBCABABCACCBCABCCBBBCCBC
BABCBAABACACBCCBBACABABBAACCBABBABBABAACBACABCCCCBCACBBCCBACABCCACBBBACACABCBBAACAAACBBBCBAABAACCBAC
CBBBBACCBCCCCBABBACABCAACAACCBBCCBBBAAAAAABACACCBCCBAACBCCCCCBCAAACCCACBACCBCBBABBABCCABCAABBBAACAAB
ABCCCCACCAACBBCCAABCBBABBAACCCABACCABACBABCAACBABBAAABBBACCAABBABCBBABCCAABABACBBACBBBBABCCCBCBACCBC
CCABCBBCCACCCACBABBACACACACACABCACACBCCACAAACCCBBBABCABCCBCABAAACACABABBAABBCCAACCCBBACBCCCBCBCCACAB
ACCCCBCCCACBCCCBCABBBBABABCBABABCBCBABAABCAAACBCCACCBAABBACBCBBBCABBCAACBACCBBBBBACBBCBBBCCAAACBAABB
CBCACAACBCBBAACCCABAABBACCCABBCCAABACBCCCCBABACBCACCCCBBAAACBABBCBCCCBCBACABBCBCCACBBCAAABAACCCAAAAA
BAABCABBACBBBAAACBCBACCBBABBABCABBCCAACCCBBBBABBAAABAABCCAACABCACACBCCBBAAABBCCCCCBBBBBABBACCCBABCBA
AAAAACCBABCBBCCCBBCABACABBBCCABCAABBCCCBCCBABCABAABABBABBBAAAAAABACCCCCBABCCAACABCAAAAABCCAAAAACCCCA
CCCACBABCABAABCCCBCAACBCCBBACBACBCCABBCCACABABACABAABBBBCCBCABCABBCBACBCBCCBABCCCBCBCBBBCBCABABABCBB
BBAABCACCCCCCACCCBCCACBAABBBACCCAABCBBABBCCBCBBCBCBBCABAABABACCAACBCABBCCBBBBBBABCCACBBAABABACABCBAC
ABBBABCBBAAACABACCABAAABACACACBCCCABBCBCBAAACCACBCBCCCACBCBACABCCCAABACCACACCBCBCCAABACABCABAAABBCCA
ACBBABCBCACCBBBACBBCACCCAABBAABCBCABBBCBAABAABAACCCCBBCBACACBABABBABBBBCBCBCBABACCCAAABABAACACBCCCBA
BCACBABBACABCABBBABCACABACCCCACBACAAACAABBCABBBCABBACCCCCCBCBCBAAABBABCCAABCCCCAABCCBAABACAACABAACBB
CAABBBBCBCABCBCBAACCACABCBCAABACCBCCBBABBAABBACACAABAABACBBBCCAABBAAACBBCCBABACAAABCBCBCABACCBCBCABB
CABAAAAACCBACBCCBBBBAABCCBAACBCCABBAACACBBAAAACBCBCACBACCABAACBABCABCBCACACCBBCAAABACBBACABCCBABBBAA
ACBABCCAAACCCCBABBAACCAAAACBBCCCACCBBACBBCAAABCBBBABBAAACACACCAAAAACBAABBAAAAABABBBBACABCCABAABCBCBC
AACCACAAABBCABCCCBAABABBCCAABCCACABACBBBCAACACBCBBCCACCCBBBBCCCCBBCCBAACBAACCCCCCBCABACACBBCBACACCBC
CABCAAACACAACCACCBBBCCACAAABAABCBACAACBBCBCBBCBBBBCACABCABACACAABABAAAABAAABAACAACCCCBCABABAACBCBBCB
'''
