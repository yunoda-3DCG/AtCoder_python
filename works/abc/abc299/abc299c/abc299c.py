n = int(input())
Ss = list(input())

isDangoSeries = False
isMoreOneStick = False
count = 0
currentMax = 0
for s in Ss:
    if s == 'o':
        isDangoSeries = True
    else:
        isDangoSeries = False
        isMoreOneStick = True
        count = 0

    if isDangoSeries:
        count += 1
        currentMax = max(currentMax, count)

if currentMax == 0 or not isMoreOneStick:
    print(-1)
else:
    print(currentMax)