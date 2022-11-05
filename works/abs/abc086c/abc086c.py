n = int(input())
t = [i for i in range(n+1)]
x = [i for i in range(n+1)]
y = [i for i in range(n+1)]
t[0] = x[0] = y[0] = 0

for i in range(1, n+1):
    t[i], x[i], y[i] = map(int, input().split())

isVisitable = True
for i in range(n):
    if (x[i] + y[i]) % 2 != t[i] % 2:
        isVisitable = False
        break

    time = t[i+1] - t[i]
    dis_x = abs(x[i+1] - x[i])
    dis_y = abs(y[i+1] - y[i])
    if dis_x > time or dis_y > time or dis_x + dis_y > time:
        isVisitable = False
        break
    if dis_x == 0 and dis_y == 0:
        if not time % 2 == 0:
            isVisitable = False
            break

if isVisitable:
    print("Yes")
else:
    print("No")