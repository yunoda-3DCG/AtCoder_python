h, w = map(int, input().split())
result = 0
for i in range(h):
    result += input().count('#')

print(result)