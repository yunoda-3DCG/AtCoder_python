t = int(input())
test = []
for i in range(t):
    n = input()
    test.append(list(map(int, input().split())))

for i in range(t):
    targets = test[i]
    count = 0
    for p in range(len(targets)):
        if targets[p] % 2 == 1:
            count += 1
    print(count)