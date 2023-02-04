n, p, q, r, s = map(int, input().split())
a = []
b = []
a = list(input().split())
b = a.copy()

b[r-1:s] = a[p-1:q]
b[p-1:q] = a[r-1:s]

print(*b)