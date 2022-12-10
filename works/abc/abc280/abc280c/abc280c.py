s = list(input())
t = list(input())

isFound = False
for i in range(len(s)):
    if not s[i] == t[i]:
        isFound = True
        print(i+1)
        break

if not isFound:
    print(len(t))