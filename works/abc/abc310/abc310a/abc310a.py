n, p, q = map(int, input().split())
Ds = list(map(int, input().split()))

discount = p - q
cheepest = min(Ds)

if discount > cheepest:
    print(q + cheepest)
else:
    print(p)