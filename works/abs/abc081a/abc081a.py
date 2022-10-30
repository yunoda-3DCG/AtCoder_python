a = map(int, list(input()))

count = 0
for t in a:
    if t == 1:
        count += 1
    
print(count)