n, t = map(int, input().split())
Cs = list(map(int, input().split()))
Rs = list(map(int, input().split()))

isPlayerOneColor = False
if Cs.count(t) > 0:
    isPlayerOneColor = False
else:
    isPlayerOneColor = True

for i, c in enumerate(Cs):
    if not isPlayerOneColor and c != t:
        Rs[i] = 0
    elif isPlayerOneColor and c != Cs[0]:
        Rs[i] = 0

print(Rs.index(max(Rs))+1)