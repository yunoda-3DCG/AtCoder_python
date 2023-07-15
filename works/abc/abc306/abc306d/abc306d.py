n = int(input())
x = []
y = []

for i in range(n):
    x_temp, y_temp = map(int, input().split())
    x.append(x_temp)
    y.append(y_temp)

class MenuSet:
    isPoison = False
    points = []
    def __init__(self, isPoison):
        self.isPoison = isPoison
        self.points = []

currentType = x[0]
menuset = []
menuset.append(MenuSet(False if x[0] == 0 else True))

for i in range(n):
    if currentType != x[i]:
        menuset.append(MenuSet(False if x[i] == 0 else True))
        currentType = x[i]

    menuset[len(menuset)-1].points.append(y[i])

def CalcMax(set:MenuSet):
    if set.isPoison:
        return max(0, max(set.points))
    else:
        result = 0
        for p in set.points:
            if p >= 0:
                result += p
        return result
    
result = 0
for s in menuset:
    result += CalcMax(s)
    print(CalcMax(s))
    
print(result)