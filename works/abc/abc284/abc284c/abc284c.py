n, m = map(int, input().split())
u = []
v = []
for i in range(m):
    t1, t2 = map(int, input().split())
    u.append(t1)
    v.append(t2)

independent = 0
for i in range(1, n+1):
    if i in u or i in v:
        pass
    else:
        independent += 1


for i in range(m):
    target_min = min(u[i], v[i])
    target_max = max(u[i], v[i])
    u = [target_min if value==target_max else value for value in u]
    v = [target_min if value==target_max else value for value in v]


print(len(set(u)) + independent)