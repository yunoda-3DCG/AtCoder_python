from math import floor

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

a.insert(0, 0)
validLength = 0
invalidLength = l
testLength = l

while invalidLength - validLength != 1:
    current = 0
    cut = 0
    for i in range(n+1):
        if a[i] - a[current] >= testLength:
            current = i
            cut += 1
        if cut == k:
            break

    if cut == k and l - a[current] >= testLength:
        validLength = testLength
        testLength = floor((invalidLength + validLength)/2)
    else:
        invalidLength = testLength
        testLength = floor(invalidLength/2)

print(validLength)