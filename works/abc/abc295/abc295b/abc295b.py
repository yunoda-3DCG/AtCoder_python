import copy

r, c = map(int, input().split())
b = []
for i in range(r):
    b.append(list(input()))

result = copy.deepcopy(b)

def SetAffectedGrids(pos_x, pos_y, size):
    for x in range(-size, size+1):
        for y in range(-size + abs(x), size - abs(x) + 1):
            if pos_x + x >= 0 and pos_x + x < c and pos_y + y >= 0 and pos_y + y < r:
                print(c, pos_x + x, r, pos_y + y)
                result[pos_x + x][pos_y + y] = '.'

for p in range(r):
    for q in range(c):
        if b[p][q] == '.':
            pass
        elif  b[p][q] == '#':
            pass
        else:
            SetAffectedGrids(p, q, int(b[p][q]))

for i in range(r):
    print(*result[i], sep='')