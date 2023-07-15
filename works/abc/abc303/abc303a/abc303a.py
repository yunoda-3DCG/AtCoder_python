n = int(input())
s = list(input())
t = list(input())

isSimilar = True
for i in range(n):
    if s[i] == '1' or s[i] == 'l':
        if t[i] == '1' or t[i] =='l':
            pass
        else:
            isSimilar = False
            break
    elif s[i] == '0' or s[i] == 'o':
        if t[i] == '0' or t[i] =='o':
            pass
        else:
            isSimilar = False
            break
    else:
        if s[i] == t[i]:
            pass
        else:
            isSimilar = False
            break

if isSimilar:
    print('Yes')
else:
    print('No')