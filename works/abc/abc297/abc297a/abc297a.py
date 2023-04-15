n, d = map(int, input().split())
t = list(map(int, input().split()))

isDoubleClick = False
time = 0
for i in range(n-1):
    if t[i+1] - t[i] <= d:
        time = t[i+1]
        isDoubleClick = True
        break

if isDoubleClick:
    print(time)
else:
    print('-1')