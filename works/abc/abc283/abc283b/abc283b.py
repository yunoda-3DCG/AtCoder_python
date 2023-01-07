n = int(input())
a = list(input().split())
q = int(input())

for i in range(q):
    query = list(input().split())
    if int(query[0]) == 1:
        a[int(query[1]) - 1] = query[2]
    elif int(query[0]) == 2:
        print(a[int(query[1]) - 1])