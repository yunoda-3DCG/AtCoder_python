n = int(input())
s = list(map(int, input().split()))

result = []
result.append(s[0])
for i in range(1, n):
    result.append(s[i] - s[i-1])

print(*result)