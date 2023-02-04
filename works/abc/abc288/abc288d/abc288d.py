n, k = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    l, r = map(int, input().split())
    target = a[l-1:r]
    isPossible = sum(target) % k

    if isPossible == 0:
        print('Yes')
    else:
        print('No')