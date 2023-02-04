n, k = map(int, input().split())
names = []
for i in range(k):
    names.append(input())

names.sort()
for i in range(k):
    print(names[i])