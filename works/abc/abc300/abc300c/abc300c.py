h, w = map(int, input().split())
Cs = [list(input()) for i in range(h)]
n = min(h, w)
result = [0 for i in range(n)]
for size in range(1, n+1):
    for i in range(size, w-size):
        for j in range(size, h-size):
            if Cs[i, j] == '#':
                pass