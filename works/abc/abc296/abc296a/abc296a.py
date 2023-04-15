n = int(input())
m = list(input())

prev = ''
isValid = True
for i in m:
    if prev == i:
        isValid = False
        break
    prev = i

if isValid:
    print('Yes')
else:
    print('No')