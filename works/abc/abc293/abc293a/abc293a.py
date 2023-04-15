s = list(input())

for i in range(int(len(s)/2)):
    x = s[2*i]
    y = s[2*i+1]
    s[2*i] = y
    s[2*i+1] = x

result = ''
for i in range(len(s)):
    result += s[i]
    
print(result)