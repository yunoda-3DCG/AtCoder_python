n, m = map(int, input().split())
As = []
for i in range(m):
    As.append(list(map(int, input().split())))
friends = [[] for i in range(n)]

for j in range(m):
    for i in range(n):
        if i == 0:
            friends[As[j][i]-1].append(As[j][i+1])
        elif i == n - 1:
            friends[As[j][i]-1].append(As[j][i-1])
        else:
            friends[As[j][i]-1].append(As[j][i+1])
            friends[As[j][i]-1].append(As[j][i-1])

result = 0
for f in friends:
    result += n - len(set(f)) - 1

result /= 2

print(int(result))