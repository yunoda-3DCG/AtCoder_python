h, w = map(int, input().split())

result = []
for i in range(h):
    col = list(map(int, input().split()))
    converted = []
    for a in col:
        if a == 0:
            converted.append('.')
        else:
            converted.append(chr(a+64))
    result.append(converted)

for i in result:
    print(*i, sep='')