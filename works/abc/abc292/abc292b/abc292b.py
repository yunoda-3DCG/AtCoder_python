n, q = map(int, input().split())
players = [0 for i in range(n)]

for i in range(q):
    event, target = map(int, input().split())
    if event == 1:
        players[target - 1] += 1
    elif event == 2:
        players[target - 1] = 2
    else:
        if players[target - 1] == 2:
            print('Yes')
        else:
            print('No')
