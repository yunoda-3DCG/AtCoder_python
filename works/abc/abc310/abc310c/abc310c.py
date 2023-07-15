n = int(input())
result = set()

for _ in range(n):
    s = input()
    result.add(min(s, s[::-1]))

print(len(result))