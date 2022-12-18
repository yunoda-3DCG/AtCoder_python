n = int(input())
s = list(input())

canceler = False
for i in range(n):
    if s[i] == '\"':
        canceler = not canceler
    elif s[i] == ',' and not canceler:
        s[i] = '.'

print(''.join(s))