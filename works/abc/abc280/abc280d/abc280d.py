k = int(input())

mult = 1
isFound = False
for i in range(2, 1000000000000):
    mult *= i
    if mult < k:
        continue
    if mult % k == 0:
        isFound = True
        print(i)
        break

if not isFound:
    print(k)