h, w = map(int, input().split())
result = []
for i in range(h):
    temp = list(input())
    for index, p in enumerate(temp):
        if p == 'T':
            if index == w-1:
                continue
            if temp[index+1] == 'T':
                temp[index] = 'P'
                temp[index+1] = 'C'
    result.append(temp)

for i in result:
    print(*i, sep='')