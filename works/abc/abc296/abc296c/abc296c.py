n, x = map(int, input().split())
a = list(map(int, input().split()))

a = list(set(a))
print(a)
isValid = False
for i, t in enumerate(a):
    for p in range(i, len(a)):
        dif = abs(t - a[p])
        print(t, a[p], dif)
        if dif == abs(x):
            isValid = True
            break
        elif dif > abs(x):
            break
    if isValid:
        break

if isValid:
    print('Yes')
else:
    print('No')