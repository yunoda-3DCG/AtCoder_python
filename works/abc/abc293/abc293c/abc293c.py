import itertools

h, w = map(int, input().split())
a = []

for i in range(h):
    a.append(list(map(int, input().split())))

rootCount = 1
for i in range(h+w-2, 1, -1):
    rootCount *= i
for i in range(h-1, 1, -1):
    rootCount /= i
for i in range(w-1, 1, -1):
    rootCount /= i

print(int(rootCount))

RU = []
for i in range(h-1):
    RU.append(0)
for i in range(w-1):
    RU.append(1)

permutated = list(itertools.combinations(RU, 18))
print(len(permutated))