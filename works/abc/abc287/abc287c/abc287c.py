n, m = map(int, input().split())
uv = []
for i in range(m):
    uv.append(list(map(int, input().split())))

p = [0 for i in range(n)]
t = [i + 1 for i in range(n)]

for i in range(m):
    p[uv[i][0] - 1] += 1
    p[uv[i][1] - 1] += 1
    minNum = min(t[uv[i][0] - 1], t[uv[i][1] - 1])
    t[uv[i][0] - 1] = minNum
    t[uv[i][1] - 1] = minNum

distincted = set(t)
if p.count(1) == 2 and p.count(2) == n - 2 and len(distincted) == 2:
    print('Yes')
else:
    print('No')