inp = list(range(1, 10000))  # set을 썻을때 890 -> set 적용 8,9,0 이렇게 나눠서 들어감

non_list = []
for i in range(1, 10001):
    if i < 10:
        non_list.append(i + i)
    elif 10 <= i < 100:
        non_list.append(i + (i // 10 + i % 10))
    elif 100 <= i < 1000:
        non_list.append(i + (i // 100 + (i % 100) // 10 + i % 10))
    elif 1000 <= i < 10000:
        if i + (i // 1000 + (i % 1000) // 100 + (i % 100) // 10 + i % 10) < 10000:
            non_list.append(i + (i // 1000 + (i % 1000) // 100 + (i % 100) // 10 + i % 10))
        else:
            continue

inp = set(inp)
non_list = set(non_list)
result_list = sorted(inp - non_list)
for result in result_list:
    print(result, sep="\n")
