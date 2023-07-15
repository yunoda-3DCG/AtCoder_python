n, m = map(int, input().split())
products = [list(map(int, input().split())) for n in range(n)]
isFound = False

for product in products:
    lessPrice = list(filter(lambda x: x[0] <= product[0], products))
    moreFunction = list(filter(lambda x: x[1] >= product[1], lessPrice))

    for candidate in moreFunction:
        matchCount = len((set(product[2:]) & set(candidate[2:])))
        if product[1] > matchCount:
            continue

        if  product[0] > candidate[0] or product[1] < candidate[1]:
            print('Yes')
            isFound = True
            break
    
    if isFound:
        break

if not isFound:
    print('No')