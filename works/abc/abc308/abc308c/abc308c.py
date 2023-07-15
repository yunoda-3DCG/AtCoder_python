n = int(input())
ratio = {}
for i in range(n):
    a, b = map(int, input().split())
    ratio[i] = a/(a+b)

dic = dict(sorted(ratio.items(), key = lambda x : x[1], reverse=True))

result = []
for k in dic.keys():
    result.append(k+1)

print(*result)