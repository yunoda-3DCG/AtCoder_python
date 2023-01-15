n = int(input())
s = []
t = []
for i in range(n):
    in1, in2 = map(str, input().split())
    s.append(in1)
    t.append(in2)

def GetIndex(l, x, default=-1):
    if x in l:
        return l.index(x)
    else:
        return default

isCan = True
m = [False for i in range(n)]
for i in range(n):
    if not isCan:
        break

    current = i
    tmp = [False for i in range(n)]
    while True:
        if tmp[current]:
            isCan = False
            break
        if m[current]:
            break
        next = GetIndex(s, t[current])
        if next == -1:
            break
        m[current] = True
        tmp[current] = True
        current = next

for q in range(len(m)):
    if not m[q]:
        isCan = False
        break

if isCan:    
    print('Yes')
else:
    print('No')