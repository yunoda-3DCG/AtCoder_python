n, q = map(int, input().split())
visiters = [0 for i in range(n)] #0 = not call, 1 = called, 2 = done
currentMin = 0

for i in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        visiters[i] = 1
    elif event[0] == 2:
        visiters[event[1]] = 2
    else:
        print(visiters)