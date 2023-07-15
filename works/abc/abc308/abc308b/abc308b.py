n, m = map(int, input().split())
Cs = list(map(str, input().split()))
Ds = list(map(str, input().split()))
Ps = list(map(int, input().split()))

result = 0
for c in Cs:
    if c in Ds:
        index = Ds.index(c)
        result += Ps[index+1]
    else:
        result += Ps[0]

print(result)