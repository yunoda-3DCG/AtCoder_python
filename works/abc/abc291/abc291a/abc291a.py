s = list(str(input()))

for i in range(len(s)):
    if str(s[i]).isupper():
        print(i+1)
        break