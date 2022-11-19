h, m = map(int, input().split())
a = int(h / 10)
b = int(h % 10)
c = int(m / 10)
d = int(m % 10)

while True:
    if a < 2:
        if b <= 5:
            break
    else:
        if c <= 3:
            break
    
    d += 1
    if d == 10:
        d = 0
        c += 1
        if c == 6:
            c = 0
            b += 1
            if a < 2:
                if b == 10:
                    b = 0
                    a += 1
            else:
                if b == 4:
                    a = b = c = d = 0

                    

result = [a*10 + b, c*10 + d]
print(*result)