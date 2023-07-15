n = int(input())
As = list(map(int, input().split()))

A3 = [[] for i in range(n)]
for i in range(len(As)):
    A3[As[i]-1].append(i+1)

dict = {}
for i in range(n):
    dict[str(i)] = A3[i][1]

dict_sorted = sorted(dict.items(), key = lambda x : x[1])

result = []
for t in dict_sorted:
    result.append(int(t[0]) + 1)

print(*result)