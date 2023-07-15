s = list(input())
n = int(input())

n_bin = list(bin(n)[2:]) 
point = len(s) - len(n_bin)

if point >= 0:
    for i in range(point):
        if s[i] == '?':
            s[i] = 0

    for i in range(point, len(s)-1):
        if s[i] == '?':
            s[i] = 1
else:
    for i in range(len(s)):
        if s[i] == '?':
            s[i] = 1

result = ''.join(s)
print(int(result, 10))