n, m, h, k = map(int, input().split())
s = list(input())
item = []
for i in range(m):
    item_pos = list(map(int, input().split()))
    item.append(item_pos)

pos_x = 0
pos_y = 0
isGameOver = False
for action in s:
    if action == 'R':
        pos_x += 1
    if action == 'L':
        pos_x -= 1
    if action == 'U':
        pos_y += 1
    if action == 'D':
        pos_y -= 1
    h -= 1
    
    if h < 0:
        isGameOver = True
        break

    if h < k and [pos_x, pos_y] in item:
        h = k
        item.remove([pos_x, pos_y])
    else:
        pass

if isGameOver:
    print('No')
else:
    print('Yes')