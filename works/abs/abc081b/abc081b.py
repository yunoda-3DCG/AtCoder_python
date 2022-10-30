numCount = int(input())
a = list(map(int, input().split()))

count = 0
isDividing = True
while isDividing == True:
    for t in range(numCount):
        if a[t] % 2 == 0:
            a[t] /= 2
        else:
            isDividing = False
            break

    if isDividing:
        count += 1

print(count)