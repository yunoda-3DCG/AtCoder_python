n = int(input())
s = []
for i in range(n):
    s.append(input())

forNumber = s.count('For')

if n - forNumber > forNumber:
    print('No')
else:
    print('Yes')