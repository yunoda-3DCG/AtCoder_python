n = int(input())
As = []
Ss = []
for i in range(n):
    s, a = map(str, input().split())
    Ss.append(s)
    As.append(int(a))

start = As.index(min(As))

for i in range(start, len(Ss)):
    print(Ss[i])

for i in range(0, start):
    print(Ss[i])