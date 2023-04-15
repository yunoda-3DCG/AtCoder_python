n = int(input())
a = [input().replace(' ', '') for _ in range(n)]
b = [input().replace(' ', '') for _ in range(n)]

def rotated(t) : return [list(x) for x in zip(*t[::-1])]

for i in range(4):
    isOK = True
    a = rotated(a)
    for p in range(n):
        for q in range(n):
            if a[p][q] == '1' and b[p][q] == '0':
                isOK = False
                break
        if not isOK:
            break
    if isOK:
        break

if isOK:
    print('Yes')
else:
    print('No')