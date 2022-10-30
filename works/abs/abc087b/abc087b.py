a = int(input())
b = int(input())
c = int(input())
v = int(input())

comb = []
for i in range(0, a + 1):
    for p in range(0, b + 1):
        for q in range(0, c + 1):
            comb.append([i, p, q])

count = 0
for t in range(len(comb)):
    if v == 500 * comb[t][0] + 100 * comb[t][1] + 50 * comb[t][2]:
        count += 1

print(count)