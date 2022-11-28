a, b = map(int, input().split())

count = 0
g = 1
prev = a

while True:
    print(count)
    t = b * count + a / g ** .5

    if prev < t:
        break   

    count += 1
    g += 1
    prev = t                                                                                                                                     

print(prev)