n, m = map(int, input().split())
s = []
t = []
for i in range(n):
    s.append(str(input()))
for i in range(m):
    t.append(str(input()))

result = 0
for p in range(n):
    for q in range(m):
        if s[p][3:6] == t[q]:
            result += 1
            break

print(result)