n = int(input())
a = list(map(int, input().split()))

index = 0
while index != len(a)-1:
    dif = a[index+1] - a[index]
    if dif > 1:
        a.insert(index+1, a[index]+1)
    elif dif < -1:
        a.insert(index+1, a[index]-1)
    index += 1
    
print(*a)