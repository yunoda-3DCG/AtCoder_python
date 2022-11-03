n, y = map(int, input().split())
a = b = c = 0
isPossible = False
for i in range(n+1):
    a = n - i
    for p in range(i+1):
        b = p
        c = i - p
        if y == 10000*a + 5000*b + 1000*c and n == a + b + c:
            print(a, b, c)
            isPossible = True
            break
    else:
        continue
    break

if not isPossible:
    print(-1, -1, -1)