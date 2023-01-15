s = list(input())

def n26(s):
    return ord(s) - 64

s.reverse()
result = 0
for i in range(len(s)):
    dif = 1
    for t in range(i):
        dif *= 26
    result += n26(s[i]) * dif

print(result)