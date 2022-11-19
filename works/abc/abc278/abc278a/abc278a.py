n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    del a[0]
    a.insert(n-1, 0)

print(*a)