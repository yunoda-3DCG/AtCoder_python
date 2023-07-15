h, w = map(int, input().split())
grid = [list(input()) for i in range(h)]

gridsWithCookie_x = []
gridsWithCookie_y = []
for p in range(h):
    for q in range(w):
        if grid[p][q] == '#':
            gridsWithCookie_x.append(q)
            gridsWithCookie_y.append(p)

startCookieArea_x = min(gridsWithCookie_x)
startCookieArea_y = min(gridsWithCookie_y)
endCookieArea_x = max(gridsWithCookie_x)
endCookieArea_y = max(gridsWithCookie_y)
for p in range(startCookieArea_y, endCookieArea_y+1):
    for q in range(startCookieArea_x, endCookieArea_x+1):
        if grid[p][q] == '.':
            print(p+1, q+1)