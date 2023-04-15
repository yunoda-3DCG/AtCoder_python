n = int(input())
a = list(map(int, input().split()))
isCalled = [False for i in range(len(a))]

for i in range(n):
    if isCalled[i]:
        pass
    else:
        isCalled[a[i]-1] = True

result = []
for i in range(n):
    if not isCalled[i]:
        result.append(i+1)

result.sort()
print(len(result))
print(*result)