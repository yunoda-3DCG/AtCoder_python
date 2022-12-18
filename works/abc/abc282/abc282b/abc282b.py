n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input().replace('o', '1').replace('x', '0'))

pair = 0
current = 0
while current < n:
    for i in range(current + 1, n):
        answerable = int(s[current], 2) | int(s[i],2)
        if str(bin(answerable)).count('1') == m:
            pair += 1
    current += 1

print(pair)