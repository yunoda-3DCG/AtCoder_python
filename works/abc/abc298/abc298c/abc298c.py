n = int(input())
box =[[] for x in range(n)]
q = int(input())

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box[query[2]-1].append(query[1])
    elif query[0] == 2:
        print(*sorted(box[query[1]-1]))
    elif query[0] == 3:
        result = []
        for index, i in enumerate(box):
            if query[1] in set(i):
                result.append(index+1)
        print(*result)