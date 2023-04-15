n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_in_C = []
b_in_C = []

ai = 0
bi = 0
for i in range(1, n+m):
    if a[ai] < b[bi]:
        ai += 1
        a_in_C.append(i)
    else:
        bi += 1
        b_in_C.append(i)

    if ai > n-1:
        b_in_C.extend([t for t in range(i+1, n+m+1)])
        break 
    elif bi > m-1:
        a_in_C.extend([t for t in range(i+1, n+m+1)])
        break

print(*a_in_C)
print(*b_in_C)