s = list(input())

length = len(s)
index = 0
result = 0
while index < length:
    if index != length - 1 and s[index] == '0' and s[index + 1] == '0':
        index += 1

    result += 1
    index += 1

print(result)