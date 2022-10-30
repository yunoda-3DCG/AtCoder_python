n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

distincted = list(set(d))
distincted.sort()

print(len(distincted))
