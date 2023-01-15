n = int(input())
s = list(input())

isEnd = False
for i in range(1, n):
    isEnd = False
    for l in range(n - i):
        if s[l] == s[l+i]:
            isEnd = True
            print(l)
            break
    if not isEnd:
        print(n-i)
    