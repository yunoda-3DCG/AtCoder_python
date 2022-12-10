s = list(input())

isSutable = True
if not len(s) == 8:
    isSutable = False

if not s[0].isupper():
    isSutable = False

for i in range(1, len(s) - 2):
    if i == 1 and s[i] == '0':
        isSutable = False
    if not s[i].isdecimal():
        isSutable = False

if not s[len(s) - 1].isupper():
    isSutable = False
 
if isSutable:
    print('Yes')
else:
    print('No')