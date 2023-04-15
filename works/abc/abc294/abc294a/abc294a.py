n = int(input())
a = list(map(int, input().split()))
result = []
for i in a:
    if i % 2 == 0:
        result.append(i)

print(*result)