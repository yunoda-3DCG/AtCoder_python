s = input()

count = len(s)
index = 0
isCreatable = True
while count > index and isCreatable:
    if count - index < 5:
        isCreatable = False
        break
    if s[index:index+5] == "dream":
        index += 5
        if count - index >= 5:
            if s[index:index+5] == "erase":
                continue            
        if count - index >= 2:
            if s[index:index+2] == "er":
                index += 2
    elif s[index:index+5] == "erase":
        index += 5
        if count - index >= 1:
            if s[index] == "r":
                index += 1
    else:
        isCreatable = False

if isCreatable:
    print("YES")
else:
    print("NO")
