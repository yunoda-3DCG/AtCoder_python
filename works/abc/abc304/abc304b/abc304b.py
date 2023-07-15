def PrintAbout(num:int):
    s = str(num)
    result = []
    for i in range(len(s)):
        if i <= 2:
            result.append(int(s[i]))
        else:
            result.append(0)

    print(*result, sep=(''))

PrintAbout(int(input()))