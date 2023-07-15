Ss = list(map(int, input().split()))

isValid = True
prev = 0
for s in Ss:
    if prev - s > 0:
        isValid = False
    if s < 100 or s > 675:
        isValid = False
    if s % 25 != 0:
        isValid = False
    prev = s

print('Yes' if isValid else 'No')