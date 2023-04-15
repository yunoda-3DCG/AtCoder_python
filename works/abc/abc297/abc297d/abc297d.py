a, b = map(int, input().split())

count = 0
while True:
    if a == b:
        break
    elif a == 0 or b == 0:
        count -= 1
        break
    elif a == 1:
        count += b - 1
        break
    elif b == 1:
        count += a - 1 
        break
    elif a < b:
        times = b // a
        b = b - a * times
        count += times
    elif a > b:
        times = a // b
        a = a - b * times
        count += times

print(count)