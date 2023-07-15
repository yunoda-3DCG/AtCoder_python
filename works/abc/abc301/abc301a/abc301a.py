n = int(input())
s = list(input())

if s.count('T') > s.count('A'):
    print('T')
elif s.count('T') < s.count('A'):
    print('A')
else:
    if s[-1] == 'T':
        print('A')
    else:
        print('T')