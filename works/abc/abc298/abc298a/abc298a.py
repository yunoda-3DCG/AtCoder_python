n = int(input())
s = list(input())

isPassed = False
isDenied = False
for i in s:
    if i == 'o':
        isPassed = True
    elif i == '-':
        pass
    elif i == 'x':
        isDenied = True

if isPassed and not isDenied:
    print('Yes')
else:
    print('No')
