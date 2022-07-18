def facto(soo):
    return soo * facto(soo - 1) if soo > 1 else 1


print(facto(int(input())))
