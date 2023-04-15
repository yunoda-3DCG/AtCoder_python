n = int(input())
w = list(map(str, input().split()))

words = ['and', 'not', 'that', 'the', 'you'] 

isMatch = False
for i in words:
    for p in w:
        if i == p:
            isMatch = True
            break
    
if isMatch:          
    print('Yes')
else:
    print('No')